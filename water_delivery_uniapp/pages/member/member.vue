<template>
  <view class="container">
    <view v-if="!user">
      <p>正在加载用户信息...</p>
    </view>
    <view v-else>
      <p>欢迎, {{ user.nickname }}</p>
      <!-- 可以在这里显示更多用户信息 -->
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      user: null,
    };
  },
  async created() {
    try {
      const token = uni.getStorageSync('token');
      if (!token) {
        uni.showToast({ title: '未登录', icon: 'none' });
        return;
      }

      const response = await new Promise((resolve, reject) => {
        uni.request({
          url: 'https://l.13982.com/user-info',
          method: 'GET',
          header: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          success: (res) => {
            if (res.statusCode === 200) {
              resolve(res.data);
            } else if (res.statusCode === 401) { // 处理未授权情况
              reject('Token 无效或已过期，请重新登录');
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
      if (error === 'Token 无效或已过期，请重新登录') {
        uni.showToast({ title: error, icon: 'none' });
        setTimeout(() => {
          uni.navigateTo({
            url: '/pages/login/login'
          });
        }, 1500);
      } else {
        uni.showToast({ title: '获取用户信息失败', icon: 'none' });
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
  flex-direction: column;
}
</style>