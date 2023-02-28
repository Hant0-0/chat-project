
    const roomName = JSON.parse(document.getElementById('room-name').textContent)
    const userName = JSON.parse(document.getElementById('username').textContent)
    const socket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + roomName
        + '/'
    )

    socket.onmessage = function (e) {
        let data = JSON.parse(e.data)

        let html = '<div class="message">';
            html += '<p class="nick">'+ data.username +'</p>';
            html += '<p class="message_send">' + data.message + '</p></div>'

        document.querySelector('#chat-log').innerHTML += html;

    }

    document.querySelector('#chat-message-submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#chat-message-input')
        const message = messageInputDom.value
        const username = messageInputDom.value

        socket.send(JSON.stringify({'message': message, 'username': userName}))
        messageInputDom.value = '';
    };