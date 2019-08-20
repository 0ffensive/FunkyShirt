console.log("Popup Draw Content");

chrome.runtime.onMessage.addListener(gotMessage)

function gotMessage(msg, sender, sendResponse)
{
    console.log(msg);
    let pelems = document.getElementsByTagName('p');
    for(ps of pelems){
        ps.innerHTML = msg.text;
    }
}