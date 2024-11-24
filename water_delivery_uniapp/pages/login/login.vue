<template>
  <view class="container">
    <button @click="onLogin" class="login-button">微信登录</button>
  </view>
</template>

<script>
import { navigateToOrSwitch } from "../../utils/navigation";

export default {
  methods: {
    async onLogin() {
      try {
        // 获取用户基本信息
        const profile = await this.getUserProfile();
        console.log("用户信息:", profile);

        // 获取微信登录凭证
        const jsCode = await this.getJsCode();
        console.log("微信登录凭证:", jsCode);

        // 调用后端登录接口
        const token = await this.callLoginAPI(profile, jsCode);

        // 保存 token
        uni.setStorageSync('token', token);

        // 跳转到会员页面
        navigateToOrSwitch({
          url: '/pages/member/member' // 目标页面路径
        });

      } catch (error) {
        console.error("登录流程失败:", error);
        uni.showToast({title: "登录失败", icon: "none"});
      }
    },

    getUserProfile() {
      return new Promise((resolve, reject) => {
        uni.getUserProfile({
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
        uni.login({
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
          uni.request({
            url: 'https://l.13982.com/wechat-login',
            method: 'POST',  // 确保方法是 POST
            header: {
              'Content-Type': 'application/json'
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
        uni.showToast({title: "登录失败", icon: "none"});
        throw err;
      }
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-button {
  width: 200px;
  height: 50px;
  background-color: #007aff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 18px;
}
</style>
