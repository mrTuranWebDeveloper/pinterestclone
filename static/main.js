const grids = document.querySelectorAll('.grid')
const headings = document.querySelectorAll('.heading .wrapper .text')

function enterScreen(index) {
    const grid = grids[index]
    const heading = headings[index]
    const gridColumns = grid.querySelectorAll('.column')

    grid.classList.add('active')

    gridColumns.forEach(element => {
    element.classList.remove('animate-before', 'animate-after')
    })

    heading.classList.remove('animate-before', 'animate-after')
}

function exitScreen(index, exitDelay) {
    const grid = grids[index]
    const heading = headings[index]
    const gridColumns = grid.querySelectorAll('.column')

    gridColumns.forEach(element => {
    element.classList.add('animate-after')
    })

    heading.classList.add('animate-after')

    setTimeout(() => {
    grid.classList.remove('active')
    }, exitDelay)
}

function setupAnimationCycle({ timePerScreen, exitDelay }) {
    const cycleTime = timePerScreen + exitDelay
    let nextIndex = 0

function nextCycle() {
    const currentIndex = nextIndex

    enterScreen(currentIndex)

    setTimeout(() => exitScreen(currentIndex, exitDelay), timePerScreen)

    nextIndex = nextIndex >= grids.length - 1 ? 0 : nextIndex + 1
    }

nextCycle()

setInterval(nextCycle, cycleTime)
}

setupAnimationCycle({
  timePerScreen: 2000, // ms
  exitDelay: 200 * 7 // ms
})


function scrollToTargetSection() {
    // Alt bölüme kaydırma
    const targetSection = document.getElementById('targetSection');
    const targetSectionOffset = targetSection.offsetTop; // Hedef elementin üst kenarının sayfanın üstünden uzaklığı
  
    window.scrollTo({
      top: targetSectionOffset,
      behavior: 'smooth'
    });
  }
  
  // <!-- sayfanın başına gitmek için gerekli js scripti -->
  
  document.querySelector(".scroll-btn-up").addEventListener("click", function() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  //scroll tuşu ile fonksiyon atama(bu kısım çalışıyor ancak bazı hatalar var)

  
    let currentSectionIndex = 0;
    const sections = document.querySelectorAll('.content, .header, .mantion, .background');


    window.addEventListener('wheel', handleScroll);
    window.addEventListener('mousewheel', handleScroll);
    window.addEventListener('DOMMouseScroll', handleScroll);

    function handleScroll(event) {
        const delta = Math.sign(event.deltaY);

        if (delta > 0) {
            currentSectionIndex = Math.min(currentSectionIndex + 1, sections.length - 1);
        } else if (delta < 0) {
            currentSectionIndex = Math.max(currentSectionIndex - 1, 0);
        }

        sections[currentSectionIndex].scrollIntoView({
            behavior: 'smooth'
        });

        event.preventDefault();
    }

