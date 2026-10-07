const ID = 'neconyan_scene_note';
const MAX_LENGTH = 2000;
let active = false;
let readyHandler = null;
let events = null;
let readyEvent = null;

function getContext() {
  const context = globalThis.SillyTavern?.getContext?.();
  if (!context?.extensionSettings || !context.eventSource) {
    throw new Error('Scene Note needs the Neconyan extension context.');
  }
  return context;
}

function mount() {
  if (!active || document.getElementById(ID)) return;
  const host = document.getElementById('extensions_settings2');
  if (!host) {
    console.warn('[Scene Note] Extension settings host is unavailable.');
    return;
  }

  const panel = document.createElement('section');
  panel.id = ID;
  panel.className = 'scene-note-settings';
  const title = document.createElement('h3');
  title.textContent = 'Scene Note';
  const help = document.createElement('p');
  help.textContent = 'A note for this account. It is not sent to the model.';
  const label = document.createElement('label');
  label.htmlFor = `${ID}_text`;
  label.textContent = 'Your note';
  const input = document.createElement('textarea');
  input.id = label.htmlFor;
  input.className = 'text_pole';
  input.rows = 5;
  input.maxLength = MAX_LENGTH;
  const saved = getContext().extensionSettings[ID];
  input.value = typeof saved?.text === 'string' ? saved.text : '';
  const save = document.createElement('button');
  save.type = 'button';
  save.className = 'menu_button';
  save.textContent = 'Save note';
  const status = document.createElement('p');
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');

  input.addEventListener('input', () => {
    status.textContent = 'Unsaved changes.';
  });
  save.addEventListener('click', () => {
    const context = getContext();
    context.extensionSettings[ID] = {
      text: input.value.slice(0, MAX_LENGTH),
    };
    context.saveSettingsDebounced();
    status.textContent = 'Save requested. Check app save errors before leaving.';
  });

  panel.append(title, help, label, input, save, status);
  host.append(panel);
}

export function activate() {
  if (active) return;
  const context = getContext();
  active = true;
  events = context.eventSource;
  readyEvent = context.eventTypes.APP_READY;
  readyHandler = mount;
  events.on(readyEvent, readyHandler);
}

export function deactivate() {
  active = false;
  if (events && readyHandler) {
    events.removeListener(readyEvent, readyHandler);
  }
  readyHandler = null;
  events = null;
  readyEvent = null;
  document.getElementById(ID)?.remove();
}
