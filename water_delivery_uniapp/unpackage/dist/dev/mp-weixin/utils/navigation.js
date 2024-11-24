"use strict";
const common_vendor = require("../common/vendor.js");
function navigateToOrSwitch(options) {
  const { url } = options;
  const tabBarPages = [
    "/pages/index/index",
    "/pages/login/login",
    "/pages/member/member"
  ];
  if (tabBarPages.includes(url)) {
    common_vendor.index.switchTab({
      url,
      success: options.success,
      fail: options.fail,
      complete: options.complete
    });
  } else {
    common_vendor.index.navigateTo({
      url,
      success: options.success,
      fail: options.fail,
      complete: options.complete
    });
  }
}
exports.navigateToOrSwitch = navigateToOrSwitch;
