# Python sails(js) websocket client
This library try to make sailsjs websocket easy to use. This library is made for socket.io v1.0.x .

Example of sails(js) controller (EngineController.js):

	connection: function(req, res) {
		var name = req.param('id');
        if (req.isSocket && req.method === 'POST') {
            sails.sockets.join(req, name, function(err){ // To be able to call by id
                    if (err) {
                            return res.serverError(err);
                    }
                    sails.sockets.join(req, 'all', function(err) { // To broadcast
                            if (err) {
                                    return res.serverError(err);
                            }
                            sails.sockets.broadcast(name, 'connection_ok');
                    });
                    return res.ok();
            });
        } else {
        	return res.badRequest('Method not allowed');
        }
	}
