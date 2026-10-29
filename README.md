# sidebar-cycle

A Hermes Desktop plugin that moves through the **left sidebar's session rows in the order you see them**: one row per key press with wrap-around, or straight to the Nth row.

| Shortcut | Action |
|---|---|
| `⌃⌘]` (Ctrl+Cmd+]) | Next sidebar session |
| `⌃⌘[` (Ctrl+Cmd+[) | Previous sidebar session |
| `⌘1`–`⌘9` | Sidebar session 1–9 |

On Windows and Linux the same keys use Ctrl alone: `Ctrl+]`, `Ctrl+[`, `Ctrl+1`–`Ctrl+9`.

The chords are fixed: they are not listed in **Settings → Keyboard Shortcuts**. The plugin reads the keys itself because Hermes Desktop's keybind store saves a plugin-registered shortcut as unbound whenever any row in that panel is edited.

### Freeing ⌘1–9

A built-in shortcut on the same chord always runs instead of the plugin. Hermes ships `⌘1`–`⌘9` on **Switch to tab N** and **Switch to profile N**, so `Sidebar session N` only fires after you clear `⌘N` from those rows in **Settings → Keyboard Shortcuts** (and from **Switch to recent session N** if you moved it there). The plugin never changes other actions' bindings itself.

## Why

The built-in `session.next` / `session.prev` walk sessions by **recency** and open the recent-session switcher HUD on repeated presses while Ctrl is held. The built-in number shortcuts count recency (`Switch to recent session N`) or the tab strip (`Switch to tab N`). When you want to move through the sidebar exactly as it is laid out — pinned rows, date groups, your manual drag order, active filters — this plugin does that instead.

## How it works

It uses only the public plugin SDK (`@hermes/plugin-sdk`):

- **Order** — a zero-size marker rendered into each session row through the `SESSION_ROW_AREAS.leading` slot. Walking the markers in document order gives the sidebar's real render order.
- **Current session** — `host.state.focusedStoredSessionId`.
- **Navigation** — `host.openSession(id)`.
- **Keys** — a `keydown` listener on `document` in the capture phase. The app's own shortcut dispatcher runs first on `window`; a key it already handled is left alone.
- **Long lists** — the Recents list is virtualized, so at the edge of the rendered window the plugin scrolls its own marker into view to render more rows before deciding to wrap.

It does not query, click, or restyle the app's own markup, so sidebar styling changes do not break it.

## Install

```bash
hermes plugins install https://github.com/devseunggwan/hermes-sidebar-cycle
hermes plugins enable sidebar-cycle
```

Then reload desktop plugins (`⌘K` → **Reload desktop plugins**) or restart Hermes Desktop.

## Requirements

Hermes Desktop with the plugin SDK session-row slots (Hermes `>=0.21.5`). Desktop-only: the Python `__init__.py` is an empty loader stub, with no tools, hooks, or environment variables.

## License

MIT
