const emojiSelectorIcon = document.getElementById('emojiSelectorIcon');
const emojiSelector = document.getElementById('emojiSelector');
const emojiList = document.getElementById('emojiList');
const emojiSearch = document.getElementById('emojiSearch');
const chatInput = document.querySelector('#comment-textarea');

emojiSelectorIcon.addEventListener('click', () =>{
    emojiSelector.classList.toggle('active');
})

fetch('https://emoji-api.com/emojis?access_key=10674f4f4aa3fdd2d0c0be03630309c4faa5590b')
    .then(res => res.json())
    .then(data => loadEmoji(data))

function loadEmoji(data) {
    data.forEach(emoji => {
        let li = document.createElement('li');
        li.setAttribute('emoji-name', emoji.slug);
        li.textContent = emoji.character;
        emojiList.appendChild(li);
    })
}

emojiSearch.addEventListener('keyup', e => {
    let value = e.target.value;
    let emojis = document.querySelectorAll('#emojiList li');
    emojis.forEach(emoji => {
        if (emoji.getAttribute('emoji-name').toLowerCase().includes(value)) {
            emoji.style.pdisplay = 'flex';
        }
        else {
            emoji.style.display = 'none';
        }
    })
})

emojiList.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') {
        const emojiValue = event.target.textContent;
        chatInput.value += emojiValue;
    }
});

console.log('emoji js working');