const ws = require("ws")
const express = require("express")

const expressServer = express()

const wsServer = new ws.Server({
    server: expressServer.listen(3000),
    host: "localhost",
    path: "/"
})

wsServer.on("connection", (w) => {
    console.log("websockekt started")
    w.on("message", (msg) => {
        const buffer = Buffer.from([0x68, 0x65, 0x6c, 0x6c, 0x6f]);
        const text = buffer.toString('utf-8');
        console.log("got message: ", text)
        //sending back the message to the client
        w.send(msg)
    })
})

expressServer.listen( () => console.log("listening..."))