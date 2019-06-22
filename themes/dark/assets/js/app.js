(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["app"],{

/***/ "./src/app.js":
/*!********************!*\
  !*** ./src/app.js ***!
  \********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue */ \"./node_modules/vue/dist/vue.esm.js\");\n/* harmony import */ var vue_async_computed__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! vue-async-computed */ \"./node_modules/vue-async-computed/dist/vue-async-computed.esm.js\");\n/* harmony import */ var vue_snotify__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! vue-snotify */ \"./node_modules/vue-snotify/vue-snotify.esm.js\");\n/* harmony import */ var _global_vue_shim__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./global-vue-shim */ \"./src/global-vue-shim.js\");\n/* harmony import */ var _router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./router */ \"./src/router/index.js\");\n/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./store */ \"./src/store/index.js\");\n/* harmony import */ var _utils_core__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./utils/core */ \"./src/utils/core.js\");\n\n\n\n\n\n\n\nvue__WEBPACK_IMPORTED_MODULE_0__[\"default\"].config.devtools = true;\nvue__WEBPACK_IMPORTED_MODULE_0__[\"default\"].config.performance = true; // Register plugins\n\nvue__WEBPACK_IMPORTED_MODULE_0__[\"default\"].use(vue_async_computed__WEBPACK_IMPORTED_MODULE_1__[\"default\"]);\nvue__WEBPACK_IMPORTED_MODULE_0__[\"default\"].use(vue_snotify__WEBPACK_IMPORTED_MODULE_2__[\"default\"]); // @TODO: Remove this before v1.0.0\n\nObject(_global_vue_shim__WEBPACK_IMPORTED_MODULE_3__[\"registerGlobalComponents\"])();\nconst app = new vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]({\n  name: 'App',\n  router: _router__WEBPACK_IMPORTED_MODULE_4__[\"default\"],\n  store: _store__WEBPACK_IMPORTED_MODULE_5__[\"default\"],\n\n  data() {\n    return {\n      globalLoading: false,\n      pageComponent: false\n    };\n  },\n\n  mounted() {\n    if (_utils_core__WEBPACK_IMPORTED_MODULE_6__[\"isDevelopment\"]) {\n      console.log('App Mounted!');\n    }\n\n    if (!window.location.pathname.includes('/login')) {\n      const {\n        $store\n      } = this;\n      Promise.all([$store.dispatch('login', {\n        username: window.username\n      }), $store.dispatch('getConfig'), $store.dispatch('getStats')]).then(([_, config]) => {\n        if (_utils_core__WEBPACK_IMPORTED_MODULE_6__[\"isDevelopment\"]) {\n          console.log('App Loaded!');\n        } // Legacy - send config.main to jQuery (received by index.js)\n\n\n        const event = new CustomEvent('medusa-config-loaded', {\n          detail: config.main\n        });\n        window.dispatchEvent(event);\n      }).catch(error => {\n        console.debug(error);\n        alert('Unable to connect to Medusa!'); // eslint-disable-line no-alert\n      });\n    }\n  }\n\n}).$mount('#vue-wrap');\n/* harmony default export */ __webpack_exports__[\"default\"] = (app);\n\n//# sourceURL=webpack:///./src/app.js?");

/***/ })

},[["./src/app.js","vendors","medusa-runtime","vendors~date-fns"]]]);