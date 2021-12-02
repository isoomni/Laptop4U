function scrollDown(i) {
    document.querySelector('.q' + (i + 1)).scrollIntoView(true);
};

function scrollUp(i) {
    document.querySelector('.q' + (i - 1)).scrollIntoView(true);
};
