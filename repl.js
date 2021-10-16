import repl from 'repl'
import net from 'net'

net.createServer(socket => {
  repl.start({
    prompt: '🔨 ',
    input: socket,
    output: process.stdout,
  }).on('exit', () => {
    socket.end()
  })
}).listen(`/tmp/node-repl.sock`)

