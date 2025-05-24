// Wait for full page load
window.addEventListener('load', () => {
  const body = document.body;
  const img = new Image();
  img.src = 'images/background.jpg'; // full quality background image

  img.onload = () => {
    // Once full image is loaded, swap background-image with full version
    body.style.backgroundImage = `
      linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
      url('images/background.jpg')
    `;
  };
});
