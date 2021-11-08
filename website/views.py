from . import socketio, app
from .checks import check_username
from flask_login import current_user
from flask_login.utils import login_required
from flask_socketio import join_room, leave_room
from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/chat')
def chat():
    username = request.args.get('username')
    roomname = request.args.get('roomname')

    if username and check_username(username):
        return render_template("chat.html", roomname=roomname, username=username, user=current_user)
    return redirect(url_for('views.home'))


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(
        f"\n\n{data['username']} has sent '{data['message']}' to room {data['roomname']}\n"
    )
    
    socketio.emit('receive_message', data, room=data['roomname'])


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(
        f"\n\n{data['username']} has joined the room {data['roomname']}\n"
    )

    join_room(data['roomname'])
    socketio.emit('join_room_announcement', data, room=data['roomname'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info(
        f"\n\n{data['username']} has left the room {data['roomname']}\n"
    )
    
    leave_room(data['roomname'])
    socketio.emit('leave_room_announcement', data, room=data['roomname'])
