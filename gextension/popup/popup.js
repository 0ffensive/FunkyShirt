console.log("Popup Sketch started");

function setup() {
    noCanvas();
    let userinput = select('#userinput');
    userinput.input(changedText);

    function changedText() {
        //message to content script
        let params = {
            active: true,
            currentWindow: true
        }
        chrome.tabs.query(params, gotTabs);

        function gotTabs(tabs) {

            let msg = { text: userinput.value() };

            chrome.tabs.sendMessage(tabs[0].id, msg);
        }
    }
}