export function navigateToOrSwitch(options) {
    const { url } = options;

    // 定义 tabBar 页面路径列表
    const tabBarPages = [
        '/pages/index/index',
        '/pages/login/login',
        '/pages/member/member'
    ];

    if (tabBarPages.includes(url)) {
        // 如果是 tabBar 页面，使用 switchTab
        uni.switchTab({
            url,
            success: options.success,
            fail: options.fail,
            complete: options.complete,
        });
    } else {
        // 否则使用 navigateTo
        uni.navigateTo({
            url,
            success: options.success,
            fail: options.fail,
            complete: options.complete,
        });
    }
}
