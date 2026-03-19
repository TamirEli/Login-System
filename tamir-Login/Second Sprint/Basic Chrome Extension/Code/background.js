chrome.runtime.onInstalled.addListener(function () {
    console.log("Message Logger Extension installed");
});

chrome.browserAction.onClicked.addListener(function (tab) {
    chrome.tabs.sendMessage(tab.id, { action: "logMessages" });
});
