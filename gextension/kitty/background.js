console.log("It is background script");

chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab) {
    console.log("Button Clicked");
    console.log(tab);
    let msg = {
        text: "Hello",
    }
    chrome.tabs.sendMessage(tab.id, msg);
}