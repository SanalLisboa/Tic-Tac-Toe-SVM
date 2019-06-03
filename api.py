
from flask import Flask, render_template, request,redirect
import flask
import classi as s
from Crypto import Random
from Crypto.Cipher import AES
import base64
from hashlib import md5
from urllib.parse import unquote

BLOCK_SIZE = 16

def unpad(data):
    return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]

def bytes_to_key(data, salt, output=48):
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]

def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))

app = flask.Flask(__name__, static_url_path = "/extra", static_folder = "extra")
app.config["DEBUG"] = True
@app.route('/', methods=['GET', 'POST'])
def home():
	moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	return render_template('index.html', len = len(moves), moves = moves, d = '')

@app.route('/play/<move>')
def play(move):
	password = "30".encode()
	move = move.replace("+", "%2")
	print(move)
	move = unquote(move)
	print(move)
	move = str(decrypt(move, password))
	move = move[2:len(move)-1]
	print(move)
	l = move.split(",")
	li = []
	for i in l:
		li.append(int(i))
	moves = li[:len(li)-1]
	test, output = s.check_moves(moves)
	if test != False:
		return render_template('index.html', len = len(moves), moves = moves, d = output)
	if int(li[-1]) == 0:
		return render_template('index.html', len = len(moves), moves = moves, d = '')
	mov = int(li[-1]) - 1
	if moves[mov] != 0:
		return render_template('index.html', len = len(moves), moves = moves, d = '')
	moves[mov] = +1
	test, output = s.check_moves(moves)
	if test != False:
		return render_template('index.html', len = len(moves), moves = moves, d = output)
	moves = s.find_best_move(moves)
	test, output = s.check_moves(moves)
	if test != False:
		return render_template('index.html', len = len(moves), moves = moves, d = output)
	return render_template('index.html', len = len(moves), moves = moves, d = '')