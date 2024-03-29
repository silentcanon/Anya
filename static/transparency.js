!function t(e, n, r) {
    function i(s, u) {
        if (!n[s]) {
            if (!e[s]) {
                var l = "function" == typeof require && require;
                if (!u && l)return l(s, !0);
                if (o)return o(s, !0);
                var a = new Error("Cannot find module '" + s + "'");
                throw a.code = "MODULE_NOT_FOUND", a
            }
            var h = n[s] = {exports: {}};
            e[s][0].call(h.exports, function (t) {
                var n = e[s][1][t];
                return i(n ? n : t)
            }, h, h.exports, t, e, n, r)
        }
        return n[s].exports
    }

    for (var o = "function" == typeof require && require, s = 0; s < r.length; s++)i(r[s]);
    return i
}({
    1: [function (t, e, n) {
        var r, i, o, s, u, l = [].indexOf || function (t) {
                for (var e = 0, n = this.length; n > e; e++)if (e in this && this[e] === t)return e;
                return -1
            };
        s = t("../lib/lodash.js"), u = t("./helpers"), i = t("./context"), o = {}, o.render = function (t, e, n, r) {
            var l, a;
            return null == e && (e = []), null == n && (n = {}), null == r && (r = {}), a = r.debug && console ? u.consoleLogger : u.nullLogger, a("Transparency.render:", t, e, n, r), t ? (s.isArray(e) || (e = [e]), t = (l = u.data(t)).context || (l.context = new i(t, o)), t.render(e, n, r).el) : void 0
        }, o.matcher = function (t, e) {
            return t.el.id === e || l.call(t.classNames, e) >= 0 || t.el.name === e || t.el.getAttribute("data-bind") === e
        }, o.clone = function (t) {
            return r(t).clone()[0]
        }, o.jQueryPlugin = u.chainable(function (t, e, n) {
            var r, i, s, u;
            for (u = [], i = 0, s = this.length; s > i; i++)r = this[i], u.push(o.render(r, t, e, n));
            return u
        }), ("undefined" != typeof jQuery && null !== jQuery || "undefined" != typeof Zepto && null !== Zepto) && (r = jQuery || Zepto, null != r && (r.fn.render = o.jQueryPlugin)), ("undefined" != typeof e && null !== e ? e.exports : void 0) && (e.exports = o), "undefined" != typeof window && null !== window && (window.Transparency = o), ("undefined" != typeof define && null !== define ? define.amd : void 0) && define(function () {
            return o
        })
    }, {"../lib/lodash.js": 7, "./context": 3, "./helpers": 5}], 2: [function (t, e, n) {
        var r, i, o, s, u, l, a, h, c = function (t, e) {
            function n() {
                this.constructor = t
            }

            for (var r in e)p.call(e, r) && (t[r] = e[r]);
            return n.prototype = e.prototype, t.prototype = new n, t.__super__ = e.prototype, t
        }, p = {}.hasOwnProperty;
        a = t("../lib/lodash"), h = t("./helpers"), e.exports = i = {
            Attributes: {}, createAttribute: function (t, e) {
                var n;
                return new (n = i.Attributes[e] || r)(t, e)
            }
        }, r = function () {
            function t(t, e) {
                this.el = t, this.name = e, this.templateValue = this.el.getAttribute(this.name) || ""
            }

            return t.prototype.set = function (t) {
                return this.el[this.name] = t, this.el.setAttribute(this.name, t.toString())
            }, t
        }(), o = function (t) {
            function e(t, e) {
                this.el = t, this.name = e, this.templateValue = this.el.getAttribute(this.name) || !1
            }

            var n, r, o, s;
            for (c(e, t), n = ["hidden", "async", "defer", "autofocus", "formnovalidate", "disabled", "autofocus", "formnovalidate", "multiple", "readonly", "required", "checked", "scoped", "reversed", "selected", "loop", "muted", "autoplay", "controls", "seamless", "default", "ismap", "novalidate", "open", "typemustmatch", "truespeed"], r = 0, o = n.length; o > r; r++)s = n[r], i.Attributes[s] = e;
            return e.prototype.set = function (t) {
                return this.el[this.name] = t, t ? this.el.setAttribute(this.name, this.name) : this.el.removeAttribute(this.name)
            }, e
        }(r), l = function (t) {
            function e(t, e) {
                var n;
                this.el = t, this.name = e, this.templateValue = function () {
                    var t, e, r, i;
                    for (r = this.el.childNodes, i = [], t = 0, e = r.length; e > t; t++)n = r[t], n.nodeType === h.TEXT_NODE && i.push(n.nodeValue);
                    return i
                }.call(this).join(""), this.children = a.toArray(this.el.children), (this.textNode = this.el.firstChild) ? this.textNode.nodeType !== h.TEXT_NODE && (this.textNode = this.el.insertBefore(this.el.ownerDocument.createTextNode(""), this.textNode)) : this.el.appendChild(this.textNode = this.el.ownerDocument.createTextNode(""))
            }

            return c(e, t), i.Attributes.text = e, e.prototype.set = function (t) {
                for (var e, n, r, i, o; e = this.el.firstChild;)this.el.removeChild(e);
                for (this.textNode.nodeValue = t, this.el.appendChild(this.textNode), i = this.children, o = [], n = 0, r = i.length; r > n; n++)e = i[n], o.push(this.el.appendChild(e));
                return o
            }, e
        }(r), u = function (t) {
            function e(t) {
                this.el = t, this.templateValue = "", this.children = a.toArray(this.el.children)
            }

            return c(e, t), i.Attributes.html = e, e.prototype.set = function (t) {
                for (var e, n, r, i, o; e = this.el.firstChild;)this.el.removeChild(e);
                for (this.el.innerHTML = t + this.templateValue, i = this.children, o = [], n = 0, r = i.length; r > n; n++)e = i[n], o.push(this.el.appendChild(e));
                return o
            }, e
        }(r), s = function (t) {
            function e(t) {
                e.__super__.constructor.call(this, t, "class")
            }

            return c(e, t), i.Attributes["class"] = e, e
        }(r)
    }, {"../lib/lodash": 7, "./helpers": 5}], 3: [function (t, e, n) {
        var r, i, o, s, u, l, a;
        a = t("./helpers"), s = a.before, o = a.after, u = a.chainable, l = a.cloneNode, i = t("./instance"), e.exports = r = function () {
            function t(t, e) {
                this.el = t, this.Transparency = e, this.template = l(this.el), this.instances = [new i(this.el, this.Transparency)], this.instanceCache = []
            }

            var e, n;
            return n = u(function () {
                return this.parent = this.el.parentNode, this.parent ? (this.nextSibling = this.el.nextSibling, this.parent.removeChild(this.el)) : void 0
            }), e = u(function () {
                return this.parent ? this.nextSibling ? this.parent.insertBefore(this.el, this.nextSibling) : this.parent.appendChild(this.el) : void 0
            }), t.prototype.render = s(n)(o(e)(u(function (t, e, n) {
                for (var r, o, s, u, a, h, c; t.length < this.instances.length;)this.instanceCache.push(this.instances.pop().remove());
                for (; t.length > this.instances.length;)u = this.instanceCache.pop() || new i(l(this.template), this.Transparency), this.instances.push(u.appendTo(this.el));
                for (c = [], s = o = 0, a = t.length; a > o; s = ++o)h = t[s], u = this.instances[s], r = [], c.push(u.prepare(h, r).renderValues(h, r).renderDirectives(h, s, e).renderChildren(h, r, e, n));
                return c
            }))), t
        }()
    }, {"./helpers": 5, "./instance": 6}], 4: [function (t, e, n) {
        var r, i, o, s, u, l, a, h, c, p, f, d = {}.hasOwnProperty, m = function (t, e) {
            function n() {
                this.constructor = t
            }

            for (var r in e)d.call(e, r) && (t[r] = e[r]);
            return n.prototype = e.prototype, t.prototype = new n, t.__super__ = e.prototype, t
        };
        p = t("../lib/lodash.js"), f = t("./helpers"), r = t("./attributeFactory"), e.exports = s = {
            Elements: {input: {}},
            createElement: function (t) {
                var e, n;
                return new (e = "input" === (n = t.nodeName.toLowerCase()) ? s.Elements[n][t.type.toLowerCase()] || u : s.Elements[n] || o)(t)
            }
        }, o = function () {
            function t(t) {
                this.el = t, this.attributes = {}, this.childNodes = p.toArray(this.el.childNodes), this.nodeName = this.el.nodeName.toLowerCase(), this.classNames = this.el.className.split(" "), this.originalAttributes = {}
            }

            return t.prototype.empty = function () {
                for (var t; t = this.el.firstChild;)this.el.removeChild(t);
                return this
            }, t.prototype.reset = function () {
                var t, e, n, r;
                n = this.attributes, r = [];
                for (e in n)t = n[e], r.push(t.set(t.templateValue));
                return r
            }, t.prototype.render = function (t) {
                return this.attr("text", t)
            }, t.prototype.attr = function (t, e) {
                var n, i;
                return n = (i = this.attributes)[t] || (i[t] = r.createAttribute(this.el, t, e)), null != e && n.set(e), n
            }, t.prototype.renderDirectives = function (t, e, n) {
                var r, i, o, s;
                o = [];
                for (i in n)d.call(n, i) && (r = n[i], "function" == typeof r && (s = r.call(t, {
                    element: this.el,
                    index: e,
                    value: this.attr(i).templateValue
                }), o.push(null != s ? this.attr(i, s) : void 0)));
                return o
            }, t
        }(), a = function (t) {
            function e(t) {
                e.__super__.constructor.call(this, t), this.elements = f.getElements(t)
            }

            return m(e, t), s.Elements.select = e, e.prototype.render = function (t) {
                var e, n, r, i, o;
                for (t = t.toString(), i = this.elements, o = [], e = 0, n = i.length; n > e; e++)r = i[e], "option" === r.nodeName && o.push(r.attr("selected", r.el.value === t));
                return o
            }, e
        }(o), c = function (t) {
            function e() {
                return e.__super__.constructor.apply(this, arguments)
            }

            var n, r, i, o;
            for (m(e, t), n = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"], r = 0, i = n.length; i > r; r++)o = n[r], s.Elements[o] = e;
            return e.prototype.attr = function (t, n) {
                return "text" !== t && "html" !== t ? e.__super__.attr.call(this, t, n) : void 0
            }, e
        }(o), u = function (t) {
            function e() {
                return e.__super__.constructor.apply(this, arguments)
            }

            return m(e, t), e.prototype.render = function (t) {
                return this.attr("value", t)
            }, e
        }(c), h = function (t) {
            function e() {
                return e.__super__.constructor.apply(this, arguments)
            }

            return m(e, t), s.Elements.textarea = e, e
        }(u), i = function (t) {
            function e() {
                return e.__super__.constructor.apply(this, arguments)
            }

            return m(e, t), s.Elements.input.checkbox = e, e.prototype.render = function (t) {
                return this.attr("checked", Boolean(t))
            }, e
        }(u), l = function (t) {
            function e() {
                return e.__super__.constructor.apply(this, arguments)
            }

            return m(e, t), s.Elements.input.radio = e, e
        }(i)
    }, {"../lib/lodash.js": 7, "./attributeFactory": 2, "./helpers": 5}], 5: [function (t, e, n) {
        var r, i, o, s;
        r = t("./elementFactory"), n.before = function (t) {
            return function (e) {
                return function () {
                    return t.apply(this, arguments), e.apply(this, arguments)
                }
            }
        }, n.after = function (t) {
            return function (e) {
                return function () {
                    return e.apply(this, arguments), t.apply(this, arguments)
                }
            }
        }, n.chainable = n.after(function () {
            return this
        }), n.onlyWith$ = function (t) {
            return "undefined" != typeof jQuery && null !== jQuery || "undefined" != typeof Zepto && null !== Zepto ? function (e) {
                return t(arguments)
            }(jQuery || Zepto) : void 0
        }, n.getElements = function (t) {
            var e;
            return e = [], i(t, e), e
        }, i = function (t, e) {
            var o, s;
            for (o = t.firstChild, s = []; o;)o.nodeType === n.ELEMENT_NODE && (e.push(new r.createElement(o)), i(o, e)), s.push(o = o.nextSibling);
            return s
        }, n.ELEMENT_NODE = 1, n.TEXT_NODE = 3, s = function () {
            return "<:nav></:nav>" !== document.createElement("nav").cloneNode(!0).outerHTML
        }, n.cloneNode = "undefined" == typeof document || null === document || s() ? function (t) {
            return t.cloneNode(!0)
        } : function (t) {
            var e, r, i, s, u;
            if (e = Transparency.clone(t), e.nodeType === n.ELEMENT_NODE)for (e.removeAttribute(o), u = e.getElementsByTagName("*"), i = 0, s = u.length; s > i; i++)r = u[i], r.removeAttribute(o);
            return e
        }, o = "transparency", n.data = function (t) {
            return t[o] || (t[o] = {})
        }, n.nullLogger = function () {
        }, n.consoleLogger = function () {
            return console.log(arguments)
        }, n.log = n.nullLogger
    }, {"./elementFactory": 4}], 6: [function (t, e, n) {
        var r, i, o, s, u = {}.hasOwnProperty;
        i = t("../lib/lodash.js"), o = (s = t("./helpers")).chainable, e.exports = r = function () {
            function t(t, e) {
                this.Transparency = e, this.queryCache = {}, this.childNodes = i.toArray(t.childNodes), this.elements = s.getElements(t)
            }

            return t.prototype.remove = o(function () {
                var t, e, n, r, i;
                for (r = this.childNodes, i = [], t = 0, e = r.length; e > t; t++)n = r[t], i.push(n.parentNode.removeChild(n));
                return i
            }), t.prototype.appendTo = o(function (t) {
                var e, n, r, i, o;
                for (i = this.childNodes, o = [], e = 0, n = i.length; n > e; e++)r = i[e], o.push(t.appendChild(r));
                return o
            }), t.prototype.prepare = o(function (t) {
                var e, n, r, i, o;
                for (i = this.elements, o = [], n = 0, r = i.length; r > n; n++)e = i[n], e.reset(), o.push(s.data(e.el).model = t);
                return o
            }), t.prototype.renderValues = o(function (t, e) {
                var n, r, o, s;
                if (i.isElement(t) && (n = this.elements[0]))return n.empty().el.appendChild(t);
                if ("object" == typeof t) {
                    o = [];
                    for (r in t)u.call(t, r) && (s = t[r], null != s && o.push(i.isString(s) || i.isNumber(s) || i.isBoolean(s) || i.isDate(s) ? function () {
                        var t, e, i, o;
                        for (i = this.matchingElements(r), o = [], t = 0, e = i.length; e > t; t++)n = i[t], o.push(n.render(s));
                        return o
                    }.call(this) : "object" == typeof s ? e.push(r) : void 0));
                    return o
                }
            }), t.prototype.renderDirectives = o(function (t, e, n) {
                var r, i, o, s;
                s = [];
                for (o in n)u.call(n, o) && (r = n[o], "object" == typeof r && ("object" != typeof t && (t = {value: t}), s.push(function () {
                    var n, s, u, l;
                    for (u = this.matchingElements(o), l = [], n = 0, s = u.length; s > n; n++)i = u[n], l.push(i.renderDirectives(t, e, r));
                    return l
                }.call(this))));
                return s
            }), t.prototype.renderChildren = o(function (t, e, n, r) {
                var i, o, s, u, l;
                for (l = [], o = 0, u = e.length; u > o; o++)s = e[o], l.push(function () {
                    var e, o, u, l;
                    for (u = this.matchingElements(s), l = [], e = 0, o = u.length; o > e; e++)i = u[e], l.push(this.Transparency.render(i.el, t[s], n[s], r));
                    return l
                }.call(this));
                return l
            }), t.prototype.matchingElements = function (t) {
                var e, n, r;
                return r = (e = this.queryCache)[t] || (e[t] = function () {
                        var e, r, i, o;
                        for (i = this.elements, o = [], e = 0, r = i.length; r > e; e++)n = i[e], this.Transparency.matcher(n, t) && o.push(n);
                        return o
                    }.call(this)), s.log("Matching elements for '" + t + "':", r), r
            }, t
        }()
    }, {"../lib/lodash.js": 7, "./helpers": 5}], 7: [function (t, e, n) {
        var r = {};
        r.toString = Object.prototype.toString, r.toArray = function (t) {
            for (var e = new Array(t.length), n = 0; n < t.length; n++)e[n] = t[n];
            return e
        }, r.isString = function (t) {
            return "[object String]" == r.toString.call(t)
        }, r.isNumber = function (t) {
            return "[object Number]" == r.toString.call(t)
        }, r.isArray = Array.isArray || function (t) {
                return "[object Array]" === r.toString.call(t)
            }, r.isDate = function (t) {
            return "[object Date]" === r.toString.call(t)
        }, r.isElement = function (t) {
            return !(!t || 1 !== t.nodeType)
        }, r.isPlainValue = function (t) {
            var e;
            return e = typeof t, "object" !== e && "function" !== e || n.isDate(t)
        }, r.isBoolean = function (t) {
            return t === !0 || t === !1
        }, e.exports = r
    }, {}]
}, {}, [1]);
/**
 * Created by Canon on 2015-08-08.
 */
