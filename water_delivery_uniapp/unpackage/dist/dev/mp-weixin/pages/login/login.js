"use strict";
const common_vendor = require("../../common/vendor.js");
const utils_navigation = require("../../utils/navigation.js");
const _sfc_main = {
  methods: {
    async onLogin() {
      try {
        const profile = await this.getUserProfile();
        console.log("用户信息:", profile);
        const jsCode = await this.getJsCode();
        console.log("微信登录凭证:", jsCode);
        const token = await this.callLoginAPI(profile, jsCode);
        common_vendor.index.setStorageSync("token", token);
        utils_navigation.navigateToOrSwitch({
          url: "/pages/member/member"
          // 目标页面路径
        });
      } catch (error) {
        console.error("登录流程失败:", error);
        common_vendor.index.showToast({ title: "登录失败", icon: "none" });
      }
    },
    getUserProfile() {
      return new Promise((resolve, reject) => {
        common_vendor.index.getUserProfile({
          desc: "用于完善会员资料",
          success: (res) => {
            console.log("获取用户信息成功:", res);
            resolve(res.userInfo);
          },
          fail: (err) => {
            console.error("获取用户信息失败:", err);
            reject("用户未授权");
          }
        });
      });
    },
    getJsCode() {
      return new Promise((resolve, reject) => {
        common_vendor.index.login({
          success: (res) => {
            if (res.code) {
              resolve(res.code);
            } else {
              reject("获取 js_code 失败");
            }
          },
          fail: (err) => {
            reject(err);
          }
        });
      });
    },
    async callLoginAPI(profile, jsCode) {
      try {
        const loginData = {
          nickname: profile.nickName,
          avatar_url: profile.avatarUrl || "",
          gender: profile.gender,
          js_code: jsCode
        };
        console.log("准备发送的登录数据:", loginData);
        const response = await new Promise((resolve, reject) => {
          common_vendor.index.request({
            url: "https://l.13982.com/wechat-login",
            method: "POST",
            // 确保方法是 POST
            header: {
              "Content-Type": "application/json"
            },
            data: loginData,
            success: (res) => {
              if (res.statusCode === 200) {
                resolve(res.data.token);
              } else {
                reject(`HTTP 响应状态码非 200: ${res.statusCode}`);
              }
            },
            fail: (err) => {
              reject(`请求失败: ${err}`);
            }
          });
        });
        return response;
      } catch (err) {
        console.error("调用登录 API 失败:", err);
        common_vendor.index.showToast({ title: "登录失败", icon: "none" });
        throw err;
      }
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: common_vendor.o((...args) => $options.onLogin && $options.onLogin(...args))
  };
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__scopeId", "data-v-e4e4508d"]]);
wx.createPage(MiniProgramPage);
