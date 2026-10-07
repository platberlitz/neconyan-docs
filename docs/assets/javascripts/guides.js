(() => {
  'use strict';

  const script = document.currentScript;
  const images = new URL('../images/', script.src);
  const guides = ['miso', 'taro', 'nori'];
  const genders = ['neutral', 'female', 'male'];
  const pronouns = { neutral: 'they/them', female: 'she/her', male: 'he/him' };
  const storageKey = 'neconyan-docs:guide-genders:v1';
  let choices = {};

  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '{}');
    if (saved && typeof saved === 'object' && !Array.isArray(saved)) choices = saved;
  } catch {
    // Reading the handbook never depends on browser storage being available.
  }

  function applyChoices() {
    for (const guide of guides) {
      const gender = genders.includes(choices[guide]) ? choices[guide] : 'neutral';
      const name = guide[0].toUpperCase() + guide.slice(1);
      const icon = new URL(`icons/${guide}-${gender}.png`, images).href;
      document.querySelectorAll(`[data-guide="${guide}"]`).forEach(image => {
        image.src = image.dataset.scene
          ? new URL(`guides/${image.dataset.scene}-${gender}.webp`, images).href
          : icon;
        if (image.alt) image.alt = `${name}, ${gender} presentation`;
      });
      document.querySelectorAll(`[data-pronouns="${guide}"]`).forEach(label => {
        label.textContent = pronouns[gender];
      });
      document.querySelectorAll(`[data-gender-select="${guide}"]`).forEach(select => {
        select.value = gender;
      });
      document.querySelectorAll(`.admonition.${guide}`).forEach(note => {
        note.style.setProperty('--guide-icon', `url("${icon}")`);
      });
    }
  }

  function initialise() {
    applyChoices();
    document.querySelectorAll('[data-gender-select]').forEach(select => {
      select.addEventListener('change', () => {
        if (!guides.includes(select.dataset.genderSelect) || !genders.includes(select.value)) return;
        choices[select.dataset.genderSelect] = select.value;
        let saved = true;
        try {
          localStorage.setItem(storageKey, JSON.stringify(choices));
        } catch {
          saved = false;
        }
        applyChoices();
        select.closest('[data-guide-settings]').querySelector('[role="status"]').textContent = saved
          ? 'Guide choices saved in this browser.'
          : 'Changed for this page. This browser could not save your choices.';
      });
    });

    const dialog = document.querySelector('.screenshot-dialog');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    document.querySelectorAll('.screenshot a').forEach(link => {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        const image = link.querySelector('img');
        dialog.querySelector('img').src = link.href;
        dialog.querySelector('img').alt = image.alt;
        dialog.querySelector('p').textContent = image.alt;
        dialog.showModal();
      });
    });
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialise, { once: true });
  else initialise();
})();
