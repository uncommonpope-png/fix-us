import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

logger = logging.getLogger("AriaObservatory")

class AriaObservatory:
    def __init__(self, master):
        self.master = master
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        self.setup_routes()
        self.thread = None

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('observatory.html')

    def start(self, host="0.0.0.0", port=5000):
        logger.info(f"Starting ARIA OBSERVATORY at http://{host}:{port}")
        self.thread = threading.Thread(target=lambda: self.socketio.run(self.app, host=host, port=port, debug=False, use_reloader=False))
        self.thread.daemon = True
        self.thread.start()

    def broadcast_update(self, event_type, data):
        """Send real-time updates to the frontend."""
        self.socketio.emit('soul_update', {'type': event_type, 'data': data})
