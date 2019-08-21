chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab) {
    let msg = {
        text: "Hello",
    }
    chrome.tabs.sendMessage(tab.id, msg);
}