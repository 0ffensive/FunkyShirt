console.log("It is content script");
chrome.runtime.onMessage.addListener(gotMessage)

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function modifyColorOfLinks() {
    let elements = document.getElementsByTagName('img');
    for (el of elements) {
        console.log(el);
        let url = chrome.runtime.getURL('images/kitty-annushka-' + getRandomInt(1,7) + '.jpg'); 
        el.src = url;
        console.log(url);
    }
}

function gotMessage(msg, sender, sendResponse)
{
    console.log(msg);
    if(msg.text === "Hello")
    {
        console.log("Replacing");
        modifyColorOfLinks();
    }
}