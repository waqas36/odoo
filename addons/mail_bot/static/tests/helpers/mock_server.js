odoo.define('mail_bot/static/tests/helpers/mock_server.js', function (require) {
"use strict";

const MockServer = require('web.MockServer');

MockServer.include({
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    async _performRpc(route, args) {
        if (args.model === 'mail.channel' && args.method === 'init_odoobot') {
            return this._mockMailChannelInitPureDigitalBot();
        }
        return this._super(...arguments);
    },

    //--------------------------------------------------------------------------
    // Private Mocked Methods
    //--------------------------------------------------------------------------

    /**
     * Simulates `init_odoobot` on `mail.channel`.
     *
     * @private
     */
    _mockMailChannelInitPureDigitalBot() {
        // TODO implement this mock task-2300480
        // and improve test "PureDigitalBot initialized after 2 minutes"
    },
});

});
