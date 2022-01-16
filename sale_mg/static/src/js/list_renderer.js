odoo.define('vt_account_tax.account_tax_pit_merge_header', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');
var core = require('web.core');


ListRenderer.include({

   _renderHeaderCell(node) {
        var th = this._super.apply(this, arguments);
        th = th.css("width", node.attrs.width);
        return th;
    },

    });

});