const socket = io()

socket.on('connect', function () {
    socket.emit('join_room', {
        username: "{{ username }}",
        roomname: "{{ roomname }}"
    })

    let messages = document.getElementById('message');
    document.getElementById('get_message').onsubmit = function (e) {
        e.preventDefault();
        let message = messages.value.trim();
        if (message) {
            socket.emit('send_message', {
                username: "{{ username }}",
                roomname: "{{ roomname }}",
                message: message
            })
        }
        messages.value = '';
        messages.focus();
    }
});

window.onbeforeunload = function () {
    socket.emit('leave_room', {
        username: "{{ username }}",
        roomname: "{{ roomname }}"
    })
};

socket.on('receive_message', function (data) {
    console.log(data);
    const newNode = document.createElement('div');
    newNode.innerHTML = "<b>" + data.username + ":&nbsp;</b>" + data.message;
    document.getElementById('show_messages').appendChild(newNode);
});

socket.on('join_room_announcement', function (data) {
    console.log(data);
    const newNode = document.createElement('div');
    newNode.innerHTML = "<b>" + data.username + "</b> has joined the room.";
    document.getElementById('show_messages').appendChild(newNode);
});

socket.on('leave_room_announcement', function (data) {
    console.log(data);
    const newNode = document.createElement('div');
    newNode.innerHTML = `<b>${data.username}</b> has left the room`;
    document.getElementById('show_messages').appendChild(newNode);
});