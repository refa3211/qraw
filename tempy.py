
import tempfile

lastqr = []


def tempofile(username):
    tempo = tempfile.TemporaryFile(delete=False, suffix='.png', prefix=f'qr-code{username}')
    lastqr.append(tempo.name)
    print(tempo)

    return tempo


print(lastqr)
tempofile('test')
print(lastqr)
tempofile('test')
print(lastqr)
tempofile('test')
print(lastqr[:1])
print(lastqr)
print(lastqr[-1])