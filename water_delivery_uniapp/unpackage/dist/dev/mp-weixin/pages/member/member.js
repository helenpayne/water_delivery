"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      user: null
    };
  },
  async created() {
    try {
      const token = common_vendor.index.getStorageSync("token");
      if (!token) {
        common_vendor.index.showToast({ title: "未登录", icon: "none" });
        return;
      }
      const response = await new Promise((resolve, reject) => {
        common_vendor.index.request({
          url: "https://l.13982.com/user-info",
          method: "GET",
          header: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
          },
          success: (res) => {
            if (res.statusCode === 200) {
              resolve(res.data);
            } else if (res.statusCode === 401) {
              reject("Token 无效或已过期，请重新登录");
            } else {
              reject(`HTTP 响应状态码非 200: ${res.statusCode}`);
            }
          },
          fail: (err) => {
            reject(`请求失败: ${err}`);
          }
        });
      });
      this.user = response;
    } catch (error) {
      console.error("获取用户信息失败:", error);
      if (error === "Token 无效或已过期，请重新登录") {
        common_vendor.index.showToast({ title: error, icon: "none" });
        setTimeout(() => {
          common_vendor.index.navigateTo({
            url: "/pages/login/login"
          });
        }, 1500);
      } else {
        common_vendor.index.showToast({ title: "获取用户信息失败", icon: "none" });
      }
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return common_vendor.e({
    a: !$data.user
  }, !$data.user ? {} : {
    b: common_vendor.t($data.user.nickname)
  });
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__scopeId", "data-v-4ca88669"]]);
wx.createPage(MiniProgramPage);
