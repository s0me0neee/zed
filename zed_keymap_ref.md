# Zed Keymap Reference

Documents every binding in [`keymap.json`](./keymap.json) — a vim-mode config ported from a
LazyVim/mini.ai Neovim setup (see [`nvim_keymap_ref.md`](./nvim_keymap_ref.md) for the source).
`space` below means the leader key (literal space bar), matching the nvim config's `<leader>`.

Generated 2026-08-06 · 49 context blocks.

## Contents

1. [Global](#global)
2. [Normal-mode motions & core editing](#normal-mode-motions--core-editing)
3. [Leader (`space`) commands](#leader-space-commands)
4. [Gitsigns (`g h` prefix)](#gitsigns-g-h-prefix)
5. [Insert mode](#insert-mode)
6. [Visual mode](#visual-mode)
7. [Replace mode](#replace-mode)
8. [Text objects (`i` / `a` / `cs`)](#text-objects-i--a--cs)
9. [Operators (second key after `d`, `c`, `y`, ...)](#operators-second-key-after-d-c-y-)
10. [Doubled-operator shortcuts (`dd`-style)](#doubled-operator-shortcuts-dd-style)
11. [Literal / digraph mode](#literal--digraph-mode)
12. [Window management (`ctrl-w` prefix)](#window-management-ctrl-w-prefix)
13. [Panels](#panels)
14. [Pickers & misc UI](#pickers--misc-ui)

---

## Global

Applies outside vim mode entirely.

| Context | Key | Action | What it does |
|---|---|---|---|
| `Workspace` | `ctrl-/` | `terminal_panel::Toggle` | Show/hide the terminal panel |

---

## Normal-mode motions & core editing

*Context: `VimControl && !menu && !Terminal`* — the broad context active whenever vim mode has
control and no menu/terminal is focused. Covers motions, the leader-key tree, marks/jumps, and
count support.

### Motions

| Key | Action | What it does |
|---|---|---|
| `h` / `left` | `vim::Left` | Move left |
| `j` / `down` | `vim::Down` | Move down |
| `k` / `up` | `vim::Up` | Move up |
| `l` / `right` | `vim::Right` | Move right |
| `w` | `vim::NextWordStart` | Jump to next word start |
| `shift-w` | `vim::NextWordStart` (ignore punctuation) | Jump to next WORD start |
| `e` | `vim::NextWordEnd` | Jump to next word end |
| `shift-e` | `vim::NextWordEnd` (ignore punctuation) | Jump to next WORD end |
| `b` | `vim::PreviousWordStart` | Jump back to previous word start |
| `shift-b` | `vim::PreviousWordStart` (ignore punctuation) | Jump back to previous WORD start |
| `g shift-e` | `vim::PreviousWordEnd` (ignore punctuation) | Jump back to previous WORD end |
| `$` | `vim::EndOfLine` | Go to end of line |
| `^` | `vim::FirstNonWhitespace` | Go to first non-blank character |
| `0` | `vim::StartOfLine` | Go to column 0 |
| `shift-g` | `vim::EndOfDocument` | Go to end of file |
| `g g` | `vim::StartOfDocument` | Go to start of file |
| `{` / `}` | `vim::StartOfParagraph` / `EndOfParagraph` | Jump paragraph up/down |
| `(` / `)` | `vim::SentenceBackward` / `SentenceForward` | Jump sentence back/forward |
| `\|` | `vim::GoToColumn` | Go to column N (with count) |
| `%` | `vim::Matching` (match quotes) | Jump to matching bracket/quote |
| `f` / `shift-f` | `vim::PushFindForward` / `PushFindBackward` | Find character forward/backward on line |
| `t` / `shift-t` | `vim::PushFindForward` (before) / `PushFindBackward` (after) | Find *till* character forward/backward |
| `;` / `,` | `vim::RepeatFind` / `RepeatFindReversed` | Repeat last f/t find, forward/reversed |
| `n` / `shift-n` | `vim::MoveToNextMatch` / `MoveToPreviousMatch` | Repeat last search, forward/backward |
| `/` | `vim::Search` | Search forward |
| `?` | `vim::Search` (backwards) | Search backward |
| `m` | `vim::PushMark` | Set a mark |
| `'` | `vim::PushJump` (line) | Jump to mark (linewise) |
| `` ` `` | `vim::PushJump` (exact) | Jump to mark (exact position) |
| `ctrl-d` / `ctrl-u` | `vim::ScrollDown` / `ScrollUp` | Scroll half-page down/up |
| `] b` / `[ b` | `pane::ActivateNextItem` / `ActivatePreviousItem` | Next/previous buffer |
| `shift-l` / `shift-h` | `pane::ActivateNextItem` / `ActivatePreviousItem` | Next/previous buffer (alt keys) |
| `1`–`9` | `vim::Number` | Count prefix for motions/operators |
| `.` | `vim::Repeat` | Repeat last change |

### Mode switches & misc editing

| Key | Action | What it does |
|---|---|---|
| `i` | `vim::PushObject` (around: false) | Text-object prefix (see [text objects](#text-objects-i--a--cs)) |
| `a` | `vim::PushObject` (around: true) | Text-object prefix |
| `escape` | `vim::SwitchToNormalMode` | Back to normal mode |
| `v` / `shift-v` / `ctrl-v` | `vim::ToggleVisual` / `ToggleVisualLine` / `ToggleVisualBlock` | Enter visual / visual-line / visual-block mode |
| `shift-k` | `editor::Hover` | Show hover docs for symbol under cursor |
| `shift-r` | `vim::ToggleReplace` | Enter Replace mode |
| `backspace` | `vim::WrappingLeft` | Move left, wrapping to previous line |
| `tab` | `vim::Tab` | Vim `<Tab>` (jumps/snippets depending on state) |
| `enter` | `menu::Confirm` | Confirm (in menu context) |
| `cmd-shift-p` | `command_palette::Toggle` | Open command palette |
| `q` | `vim::ToggleRecord` | Start/stop macro recording |
| `shift-q` | `vim::ReplayLastRecording` | Replay last macro |
| `@` | `vim::PushReplayRegister` | Replay macro from register |

### `g`-prefixed LSP & navigation

| Key | Action | What it does |
|---|---|---|
| `g d` | `editor::GoToDefinition` | Go to definition |
| `g shift-d` | `editor::GoToDeclaration` | Go to declaration |
| `g shift-i` | `editor::GoToImplementation` | Go to implementation |
| `g y` | `editor::GoToTypeDefinition` | Go to type definition |
| `g r` | `editor::FindAllReferences` | Find all references |
| `g f` | `editor::OpenSelectedFilename` | Open the filename under the cursor |
| `g shift-k` | `editor::ShowSignatureHelp` | Show function signature help |
| `g shift-o` | `outline::Toggle` | Open buffer symbol outline |
| `g n` / `g shift-n` | `vim::SelectNextMatch` / `SelectPreviousMatch` | Extend visual selection to next/prev search match |
| `] h` / `[ h` | `editor::GoToHunk` / `GoToPreviousHunk` | Jump to next/previous git diff hunk |
| `] d` / `[ d` | `editor::GoToDiagnostic` / `GoToPreviousDiagnostic` | Jump to next/previous diagnostic |

### `z`-prefixed scroll & fold commands

| Key | Action | What it does |
|---|---|---|
| `z enter` / `z t` | `workspace::SendKeystrokes("z t ^")` | Scroll line to top, cursor to first non-blank |
| `z b` | `editor::ScrollCursorBottom` | Scroll line to bottom of window |
| `z a` / `z shift-a` | `editor::ToggleFold` / `ToggleFoldRecursive` | Toggle fold / toggle fold recursively |
| `z o` / `z shift-o` | `editor::UnfoldLines` / `UnfoldRecursive` | Open fold / open fold recursively |
| `z f` | `editor::FoldSelectedRanges` | Create a fold from selection |
| `z shift-m` / `z shift-r` | `editor::FoldAll` / `UnfoldAll` | Fold/unfold everything |
| `z shift-l` / `z shift-h` | `vim::HalfPageRight` / `HalfPageLeft` | Scroll half a page right/left |

---

## Leader (`space`) commands

All leader commands live in the same broad `VimControl` context as the motions above, plus a
second batch in `vim_mode == normal` (marked below) for window/buffer management.

### Files & search

| Key | Action | What it does |
|---|---|---|
| `space space` / `space f f` | `file_finder::Toggle` | Fuzzy-find files in the project |
| `space f n` | `workspace::NewFile` | New untitled file |
| `space f t` | `terminal_panel::Toggle` | Toggle terminal panel |
| `space f c` | `zed::OpenSettingsFile` | Open `settings.json` |
| `space f b` | `tab_switcher::Toggle` | Open buffer/tab switcher |
| `space p` / `space f p` | `projects::OpenRecent` | Open recent projects picker |
| `space e` / `space shift-e` | `workspace::ToggleLeftDock` | Toggle the project panel (file tree) |
| `space /` | `pane::DeploySearch` | Open in-pane project search |
| `space s g` | `pane::DeploySearch` | Project-wide grep |
| `space s s` | `outline::Toggle` | Buffer symbol outline |
| `space s shift-s` | `project_symbols::Toggle` | Project-wide symbol search |
| `space s r` | `pane::DeploySearch` (replace mode) | Project-wide search & replace |
| `space s k` | `zed::OpenKeymap` | Open the keymap editor/viewer |
| `space s b` | `go_to_line::Toggle` | Jump to a specific line number |
| `space s shift-r` | `workspace::ReopenLastPicker` | Reopen the last picker you used |

### Code & LSP

| Key | Action | What it does |
|---|---|---|
| `space c r` | `editor::Rename` | Rename symbol |
| `space c a` | `editor::ToggleCodeActions` | Show code actions menu |
| `space c f` | `editor::Format` | Format buffer |
| `space c g` | `agent::ToggleFocus` | Toggle the AI agent panel |
| `space c l` | `lsp_tool::ToggleMenu` | Open the LSP status/tools menu |
| `space c p` | `markdown::OpenPreview` | Open Markdown preview |
| `space x x` | `diagnostics::Deploy` | Open the diagnostics panel |

### Git

| Key | Action | What it does |
|---|---|---|
| `space g b` | `editor::BlameHover` | Show inline git blame for current line |
| `space g g` | `git_panel::ToggleFocus` | Open/focus the git panel |
| `space g d` | `git::Diff` | Show diff for current file |
| `space g shift-d` | `git::ReviewDiff` | Review diff against a reference (e.g. main) |
| `space g s` | `git_panel::ActivateChangesTab` | Focus the "Changes" tab (git status) |
| `space g shift-s` | `git_picker::ActivateStashTab` | Open the git stash picker |
| `space g l` | `git_panel::ActivateHistoryTab` | Focus the "History" tab (git log) |

See also the [gitsigns `g h` cluster](#gitsigns-g-h-prefix) for hunk-level git actions.

### Debug (nvim-dap equivalent)

| Key | Action | What it does |
|---|---|---|
| `space d b` | `editor::ToggleBreakpoint` | Toggle breakpoint on current line |
| `space d shift-b` | `editor::EditLogBreakpoint` | Add/edit a log breakpoint |
| `space d c` | `debugger::Continue` | Continue execution |
| `space d i` | `debugger::StepInto` | Step into |
| `space d o` | `debugger::StepOut` | Step out |
| `space d shift-o` | `debugger::StepOver` | Step over |
| `space d shift-p` | `debugger::Pause` | Pause execution |
| `space d t` | `debugger::Stop` | Stop/terminate debug session |
| `space d l` | `debugger::Restart` | Restart last debug session |
| `space d r` / `space d u` | `debug_panel::ToggleFocus` | Toggle/focus the debug panel (REPL + Dap-UI equivalent) |
| `space d s` | `debugger::ToggleSessionPicker` | Pick between active debug sessions |
| `space d w` | `debugger::ToggleExpandItem` | Expand/collapse a debug tree item (widgets) |
| `space d e` | `console::WatchExpression` | Add a watch expression |

### UI toggles

Most of LazyVim's `<leader>u` toggles are `settings.json`-only in Zed (no runtime command exists —
e.g. relative line numbers, indent guides, treesitter highlighting, conceal, spelling, mini-pairs).
These are the ones that *do* have a real Zed action:

| Key | Action | What it does |
|---|---|---|
| `space t` / `space u shift-c` | `theme_selector::Toggle` | Open theme picker |
| `space u b` | `theme::ToggleMode` | Toggle light/dark theme mode |
| `space u h` | `editor::ToggleInlayHints` | Toggle inlay hints |
| `space u l` | `editor::ToggleLineNumbers` | Toggle line numbers |
| `space u w` | `editor::ToggleSoftWrap` | Toggle soft line wrap |
| `space u z` | `workspace::ToggleAllDocks` | Hide/show all docks (zen-mode-ish, focuses the editor) |
| `space u shift-z` / `space w m` | `vim::MaximizePane` | Toggle zoom on the active pane |

### Misc

| Key | Action | What it does |
|---|---|---|
| `space r` | `task::Spawn` | Run a project task |
| `space q q` | `workspace::CloseWindow` | Close the window (quit-all equivalent) |

### Window & buffer management *(context: `vim_mode == normal`)*

| Key | Action | What it does |
|---|---|---|
| `space w v` | `pane::SplitVertical` | Split pane vertically |
| `space w s` | `pane::SplitHorizontal` | Split pane horizontally |
| `space w d` | `pane::CloseActiveItem` | Close active pane/tab |
| `space w m` | `vim::MaximizePane` | Toggle pane zoom |
| `space b d` | `pane::CloseActiveItem` | Close current buffer |
| `space b o` | `pane::CloseOtherItems` | Close all other buffers |
| `space b b` | `pane::AlternateFile` | Switch to alternate (last) buffer |
| `space b j` | `tab_switcher::Toggle` | Pick a buffer from a list |
| `space b p` | `pane::TogglePinTab` | Pin/unpin current tab |
| `space b shift-p` | `pane::CloseAllItems` (keep pinned) | Close all non-pinned buffers |
| `space b r` | `pane::CloseItemsToTheRight` (keep pinned) | Close buffers to the right |
| `space b l` | `pane::CloseItemsToTheLeft` (keep pinned) | Close buffers to the left |
| `space ,` | `tab_switcher::ToggleAll` | Open buffer picker (all buffers) |

---

## Gitsigns (`g h` prefix)

*Context: broad `VimControl` block.* Hunk- and file-level git actions, mirroring gitsigns.nvim's
`gh` mappings.

| Key | Action | What it does |
|---|---|---|
| `g h shift-b` | `git::Blame` | Full blame view for the buffer |
| `g h d` | `git::Diff` | Diff current file |
| `g h shift-d` | `git::ReviewDiff` | Review diff against a reference |
| `g h shift-r` | `git::RestoreFile` | Discard all changes in the file |
| `g h r` | `git::Restore` | Discard the hunk under the cursor |
| `g h s` | `git::ToggleStaged` | Stage/unstage the hunk under the cursor |
| `g h shift-s` | `git::StageFile` | Stage the whole file |
| `g h u` | `git::UnstageFile` | Unstage the whole file |

---

## Insert mode

*Context: `Editor && vim_mode == insert`*

| Key | Action | What it does |
|---|---|---|
| `enter` | `editor::Newline` | Insert newline |
| `backspace` | `editor::Backspace` | Delete character before cursor |
| `escape` | `vim::NormalBefore` | Exit to normal mode |

*Context: `vim_mode == insert && !(showing_code_actions \|\| showing_completions)`*

| Key | Action | What it does |
|---|---|---|
| `ctrl-p` / `ctrl-n` | `editor::ShowWordCompletions` | Trigger word completion |

*Context: signature help showing, insert or normal mode*

| Key | Action | What it does |
|---|---|---|
| `ctrl-p` / `ctrl-n` | `editor::SignatureHelpPrevious` / `SignatureHelpNext` | Cycle overloads in signature help |

---

## Visual mode

*Context: `vim_mode == visual`*

| Key | Action | What it does |
|---|---|---|
| `d` / `x` / `backspace` / `delete` | `vim::VisualDelete` | Delete selection |
| `shift-d` | `vim::VisualDeleteLine` | Delete selected lines |
| `y` | `vim::VisualYank` | Yank selection |
| `shift-y` | `vim::VisualYankLine` | Yank selected lines |
| `p` | `vim::Paste` | Paste over selection |
| `shift-p` | `vim::Paste` (preserve clipboard) | Paste over selection, keep clipboard |
| `c` | `vim::Substitute` | Delete selection and enter insert mode |
| `shift-r` | `vim::SubstituteLine` | Delete selected lines and enter insert mode |
| `~` | `vim::ChangeCase` | Toggle case of selection |
| `ctrl-a` / `ctrl-x` | `vim::Increment` / `Decrement` | Increment/decrement numbers in selection |
| `cmd-c` / `cmd-v` | `editor::Copy` / `editor::Paste` | OS-clipboard copy/paste |
| `shift-i` / `shift-a` | `vim::InsertBefore` / `InsertAfter` | Insert at start/end of each selected line (block mode) |
| `shift-j` | `vim::JoinLines` | Join selected lines |
| `r` | `vim::PushReplace` | Replace each selected char with the next keypress |
| `s` | `vim::PushSneak` | Sneak motion (2-char jump; see note below) |
| `>` / `<` | `vim::Indent` / `Outdent` | Indent/outdent selection |
| `i` / `a` | `vim::PushObject` | Text-object prefix |
| `g c` | `vim::ToggleComments` | Toggle comment on selection |
| `"` | `vim::PushRegister` | Choose register for next yank/delete/paste |
| `escape` | `vim::SwitchToNormalMode` | Exit visual mode |

> **Note on `s`/`shift-s`:** this config uses Zed's built-in Sneak motion as a flash.nvim
> replacement, which means `s`/`S` no longer do vim's substitute-character/line. Use `cl`/`cc`
> for that instead — this is a deliberate tradeoff, documented inline in `keymap.json`.

---

## Replace mode

*Context: `vim_mode == replace`*

| Key | Action | What it does |
|---|---|---|
| `escape` / `ctrl-c` / `ctrl-[` | `vim::NormalBefore` | Exit replace mode |
| `ctrl-k` | `vim::PushDigraph` | Insert a digraph (e.g. `e:` → `ë`) |
| `ctrl-v` / `ctrl-q` / `ctrl-shift-q` | `vim::PushLiteral` | Insert next keypress literally |
| `ctrl-shift-v` | `editor::Paste` | Paste (Linux-style alt to `ctrl-v`, which is taken by literal-insert) |
| `backspace` | `vim::UndoReplace` | Undo last replaced character |
| `tab` | `vim::Tab` | Vim `<Tab>` |
| `enter` | `vim::Enter` | Vim `<CR>` |
| `insert` | `vim::InsertBefore` | Switch to plain insert mode |

---

## Text objects (`i` / `a` / `cs`)

*Context: `vim_operator == a || vim_operator == i || vim_operator == cs`* — the key pressed after
`i`/`a` (or after `cs`/`ys`/`ds` surround commands) selects **what** to operate on. E.g. `d i w`
deletes inside a word, `c a "` changes around double quotes.

| Key | Action | What it does |
|---|---|---|
| `w` | `vim::Word` | A word |
| `shift-w` | `vim::Word` (ignore punctuation) | A WORD |
| `t` | `vim::Tag` | An HTML/XML tag |
| `s` | `vim::Sentence` | A sentence |
| `p` | `vim::Paragraph` | A paragraph |
| `'` / `` ` `` / `"` / `q` | `vim::MiniQuotes` | Nearest quoted string (searches the line, mini.ai-style — see note below) |
| `\|` | `vim::VerticalBars` | Text between `\|...\|` |
| `(` / `)` | `vim::Parentheses` | Inside/around `(...)` |
| `[` / `]` | `vim::SquareBrackets` | Inside/around `[...]` |
| `{` / `}` / `shift-b` | `vim::CurlyBrackets` | Inside/around `{...}` |
| `<` / `>` | `vim::AngleBrackets` | Inside/around `<...>` |
| `b` | `vim::MiniBrackets` | Nearest bracket of **any** type (mini.ai default, not just parens) |
| `r` | `vim::SquareBrackets` | Alias for square brackets |
| `a` | `vim::Argument` | A function argument |
| `i` | `vim::IndentObj` | Lines at the same indent level |
| `shift-i` | `vim::IndentObj` (include below) | Same-indent lines, including the line below |
| `f` | `vim::Method` | A function/method |
| `c` | `vim::Class` | A class |
| `e` | `vim::Subword` | A subword (mini.ai custom object — `camelCase`/`snake_case` piece) |
| `g` | `vim::EntireFile` | The entire buffer (mini.ai custom object) |

> **Quote objects:** plain `vim::Quotes`/`vim::DoubleQuotes`/`vim::BackQuotes` only work when the
> cursor is already *between* the quotes. `vim::MiniQuotes` adds the "search the current line,
> jump to the nearest pair" behavior real Neovim (via mini.ai) gives you by default, so all three
> quote keys plus `q` are bound to it. Known limitation: it can only find quotes in languages
> whose tree-sitter grammar ships a `brackets.scm` query (e.g. no support in `.lua` or `.toml`
> files — that's a Zed/tree-sitter gap, not fixable from this file).

---

## Operators (second key after `d`, `c`, `y`, ...)

These contexts fire once an operator is pending and a *non-object* second key is pressed
(surrounds, git hunk actions, exchange, etc. — as opposed to the `i`/`a` object table above).

*Context: `vim_operator == c`*

| Key | Action | What it does |
|---|---|---|
| `x` | `vim::Exchange` | Mark/execute an exchange (`cx`) |
| `d` | `editor::Rename` | Zed-specific: `cd` triggers rename |
| `s` | `vim::PushChangeSurrounds` | `cs` — change surrounding pair (e.g. `cs"'`) |

*Context: `vim_operator == d`*

| Key | Action | What it does |
|---|---|---|
| `s` | `vim::PushDeleteSurrounds` | `ds` — delete surrounding pair |
| `v` | `vim::PushForcedMotion` | `dv` — force next motion to be characterwise |
| `o` | `editor::ToggleSelectedDiffHunks` | `do` — toggle diff hunk (vim's diffget analog) |
| `shift-o` | `git::ToggleStaged` | `dO` — stage/unstage hunk |
| `p` | `git::Restore` | `dp` — restore/discard hunk (vim's diffput analog) |
| `u` | `git::StageAndNext` | `du` — stage hunk and move to next |
| `shift-u` | `git::UnstageAndNext` | `dU` — unstage hunk and move to next |

*Context: `vim_operator == y`*

| Key | Action | What it does |
|---|---|---|
| `v` | `vim::PushForcedMotion` | `yv` — force characterwise motion |
| `s` | `vim::PushAddSurrounds` | `ys` — add surrounding pair (e.g. `ysiw"`) |

*Context: `vim_mode == waiting`*

| Key | Action | What it does |
|---|---|---|
| `s` | `vim::PushSneak` | Sneak 2-char motion |
| `tab` / `enter` | `vim::Tab` / `vim::Enter` | Passthrough |
| `escape` | `vim::ClearOperators` | Cancel pending operator |

*Context: `Editor && vim_mode == waiting && (vim_operator == ys \|\| vim_operator == cs)`*

| Key | Action | What it does |
|---|---|---|
| `escape` | `vim::SwitchToNormalMode` | Cancel a pending surround operation |

*Context: `vim_mode == operator`*

| Key | Action | What it does |
|---|---|---|
| `g c` | `vim::Comment` | Comment-toggle operator (`gc` + motion) |
| `escape` / `ctrl-c` / `ctrl-[` | `vim::ClearOperators` | Cancel pending operator |

---

## Doubled-operator shortcuts (`dd`-style)

Each of these contexts handles "operator applied to the current line" (typing the operator key
twice, or its line-shortcut) plus a couple of Zed-specific extras.

| Context | Keys | Action | What it does |
|---|---|---|---|
| `vim_operator == gu` | `g u` / `u` | `vim::CurrentLine` | `guu` — lowercase current line |
| `vim_operator == gU` | `g shift-u` / `shift-u` | `vim::CurrentLine` | `gUU` — uppercase current line |
| `vim_operator == g~` | `g ~` / `~` | `vim::CurrentLine` | `g~~` — toggle case, current line |
| `vim_operator == g?` | `g ?` / `?` | `vim::CurrentLine` | `g??` — ROT13, current line |
| `vim_operator == gq` | `g q`/`q`/`g w`/`w` | `vim::CurrentLine` | `gqq`/`gww` — format current line |
| `vim_operator == ys` | `s` | `vim::CurrentLine` | `yss` — surround current line |
| `vim_operator == >` | `>` | `vim::CurrentLine` | `>>` — indent current line |
| `vim_operator == <` | `<` | `vim::CurrentLine` | `<<` — outdent current line |
| `vim_operator == eq` | `=` | `vim::CurrentLine` | `==` — auto-indent current line |
| `vim_operator == sh` | `!` | `vim::CurrentLine` | `!!` — filter current line through shell |
| `vim_operator == gc` | `c` | `vim::CurrentLine` | `gcc` — comment-toggle current line |
| `vim_operator == gR` | `r` / `shift-r` | `vim::CurrentLine` | `gRR` — virtual replace current line |
| `vim_operator == cx` | `x` | `vim::CurrentLine` | `cxx` — exchange current line |
| `vim_operator == cx` | `c` | `vim::ClearExchange` | `cxc` — clear pending exchange |
| (normal mode) | `g c c` | `vim::ToggleComments` | Toggle comment on current line |

---

## Literal / digraph mode

*Context: `vim_mode == literal`* (entered via `ctrl-v`/`ctrl-q` in replace mode, or `ctrl-k` for
digraphs). Every `ctrl-<letter>` key inserts its literal control character (`vim::Literal`) instead
of triggering its usual binding — e.g. `ctrl-c` inserts `` instead of copying. Also covers
`escape` (→ ``), `enter` (→ ``), `tab` (→ `	`), `backspace` (→ ``), and
`delete` (→ ``, a Zed-specific extension beyond stock vim).

---

## Window management (`ctrl-w` prefix)

*Context: `VimControl && !menu || !Editor && !Terminal`* — full vim window-command emulation.
`ctrl-w` itself is unbound (`null`) so it can act as a prefix.

| Key(s) | Action | What it does |
|---|---|---|
| `ctrl-w h`/`ctrl-h`/`left` | `workspace::ActivatePaneLeft` | Focus pane to the left |
| `ctrl-w l`/`ctrl-l`/`right` | `workspace::ActivatePaneRight` | Focus pane to the right |
| `ctrl-w k`/`ctrl-k`/`up` | `workspace::ActivatePaneUp` | Focus pane above |
| `ctrl-w j`/`ctrl-j`/`down` | `workspace::ActivatePaneDown` | Focus pane below |
| `ctrl-w shift-h/j/k/l` or `shift-left/right/up/down` | `workspace::SwapPaneLeft/Right/Up/Down` | Swap panes in a direction |
| `ctrl-w x` / `ctrl-w ctrl-x` | `workspace::SwapPaneAdjacent` | Swap with adjacent pane |
| `ctrl-w shift-h/l/k/j` (move variant)* | `workspace::MovePaneLeft/Right/Up/Down` | Move current pane in a direction |
| `ctrl-w >` / `<` | `vim::ResizePaneRight` / `ResizePaneLeft` | Resize pane width |
| `ctrl-w -` / `+` | `vim::ResizePaneDown` / `ResizePaneUp` | Resize pane height |
| `ctrl-w _` | `vim::MaximizePane` | Maximize/zoom current pane |
| `ctrl-w =` | `vim::ResetPaneSizes` | Reset all pane sizes to equal |
| `ctrl-w g t` / `ctrl-w g shift-t` | `pane::ActivateNextItem` / `ActivatePreviousItem` | Next/previous tab |
| `ctrl-w w` / `ctrl-w p` | `workspace::ActivateNextPane` / `ActivatePreviousPane` | Cycle pane focus forward/backward |
| `ctrl-w v` / `ctrl-w s` | `pane::SplitVertical` / `SplitHorizontal` | Split window |
| `ctrl-w c` / `ctrl-w q` | `pane::CloseActiveItem` | Close current pane's item |
| `ctrl-w a` | `pane::CloseAllItems` | Close all items |
| `ctrl-w o` | `workspace::CloseInactiveTabsAndPanes` | Close everything except current (vim's `:only`) |
| `ctrl-w n` | `workspace::NewFileSplitHorizontal` | New file in a horizontal split |
| `g t` / `g shift-t` | `vim::GoToTab` / `GoToPreviousTab` | Next/previous tab |

\* Zed maps both "swap" and "move" vim commands to directional shift-chords; see `keymap.json` for
the exact `ctrl-w`-prefixed vs. bare-arrow key distinctions.

*Context: `VimControl && !menu || !Editor`* (works even inside the terminal)

| Key | Action | What it does |
|---|---|---|
| `ctrl-h` / `ctrl-j` / `ctrl-k` / `ctrl-l` | `workspace::ActivatePaneLeft/Down/Up/Right` | Direct pane navigation without the `ctrl-w` prefix (overrides shell's backspace/enter/kill-line/clear-screen bindings intentionally) |

*Context: `!Editor && !Terminal`*

| Key | Action | What it does |
|---|---|---|
| `:` | `command_palette::Toggle` | Open command palette |
| `g /` | `pane::DeploySearch` | Project search |
| `] b` / `[ b` | `pane::ActivateNextItem` / `ActivatePreviousItem` | Next/previous tab |
| `] shift-b` / `[ shift-b` | `pane::ActivateLastItem` / `ActivateItem(0)` | Jump to last/first tab |

---

## Panels

### Project panel (file tree) — neo-tree-style bindings

*Context: `ProjectPanel && not_editing`*

| Key | Action | What it does |
|---|---|---|
| `j` / `k` / `down` / `up` | `vim::MenuSelectNext` / `MenuSelectPrevious` | Move selection |
| `h` / `left` | `project_panel::CollapseSelectedEntry` | Collapse folder |
| `l` / `t` | `project_panel::OpenPermanent` | Open file |
| `enter` | `project_panel::OpenPermanent` | Open file |
| `v` | `project_panel::OpenSplitVertical` | Open in vertical split |
| `o` | `project_panel::OpenSplitHorizontal` | Open in horizontal split |
| `s` | `workspace::OpenWithSystem` | Open with default system app |
| `a` | `project_panel::NewFile` | New file |
| `shift-a` | `project_panel::NewDirectory` | New directory |
| `%` | `project_panel::NewFile` | New file (netrw-style) |
| `d` | `project_panel::Delete` | Delete |
| `shift-d` | `project_panel::Trash` | Move to trash (soft delete) |
| `y` / `x` / `p` | `project_panel::Copy` / `Cut` / `Paste` | Copy/cut/paste entries |
| `r` / `shift-r` | `project_panel::Rename` | Rename |
| `shift-x` | `project_panel::RevealInFileManager` | Reveal in Finder |
| `/` | `project_panel::NewSearchInDirectory` | Search within this directory |
| `z d` | `project_panel::CompareMarkedFiles` | Diff two marked files |
| `] c` / `[ c` | `project_panel::SelectNextGitEntry` / `SelectPrevGitEntry` | Jump between changed files |
| `] d` / `[ d` | `project_panel::SelectNextDiagnostic` / `SelectPrevDiagnostic` | Jump between files with diagnostics |
| `}` / `{` | `project_panel::SelectNextDirectory` / `SelectPrevDirectory` | Jump between directories |
| `shift-g` / `g g` | `menu::SelectLast` / `SelectFirst` | Jump to last/first entry |
| `-` / `backspace` | `project_panel::SelectParent` | Go to parent directory |
| `ctrl-u` / `ctrl-d` | `project_panel::ScrollUp` / `ScrollDown` | Scroll panel |
| `z t` / `z z` / `z b` | `project_panel::ScrollCursorTop/Center/Bottom` | Reposition scroll around selection |
| `escape` | `vim::ToggleProjectPanelFocus` | Leave the panel |
| `space e` | `workspace::ToggleLeftDock` | Close the panel |
| `:` | `command_palette::Toggle` | Open command palette |
| `0`–`9` | `vim::Number` | Count prefix |

### Outline panel

*Context: `OutlinePanel && not_editing`*

| Key | Action | What it does |
|---|---|---|
| `j` / `k` / `down` / `up` | `vim::MenuSelectNext` / `MenuSelectPrevious` | Move selection |
| `h` / `left` / `backspace` | `outline_panel::CollapseSelectedEntry` / `SelectParent` | Collapse / go to parent |
| `l` | `outline_panel::ExpandSelectedEntry` | Expand entry |
| `enter` | `editor::ToggleFocus` | Jump to symbol in editor |
| `/` | `menu::Cancel` | Close panel |
| `shift-g` / `g g` | `menu::SelectLast` / `SelectFirst` | Jump to last/first entry |
| `-` | `outline_panel::SelectParent` | Go to parent |
| `ctrl-u` / `ctrl-d` | `outline_panel::ScrollUp` / `ScrollDown` | Scroll panel |
| `z t` / `z z` / `z b` | `outline_panel::ScrollCursorTop/Center/Bottom` | Reposition scroll |
| `0`–`9` | `vim::Number` | Count prefix |

*Context: `OutlinePanel && editing`*

| Key | Action | What it does |
|---|---|---|
| `enter` | `menu::Cancel` | Cancel rename/edit |

### Git panel

*Context: `GitPanel && ChangesList`*

| Key | Action | What it does |
|---|---|---|
| `j` / `k` | `menu::SelectNext` / `SelectPrevious` | Move selection |
| `g g` / `shift-g` | `menu::SelectFirst` / `SelectLast` | Jump to first/last entry |
| `g f` | `menu::Confirm` | Open selected file |
| `i` | `git_panel::FocusEditor` | Focus the commit-message editor |
| `x` | `git::ToggleStaged` | Stage/unstage selected file |
| `shift-x` | `git::StageAll` | Stage everything |
| `shift-u` | `git::UnstageAll` | Unstage everything |
| `g x` | `git::StageRange` | Stage a range of selected entries |

### Settings window

*Context: `SettingsWindow > NavigationMenu && !search`*

| Key | Action | What it does |
|---|---|---|
| `j` / `k` | `settings_editor::FocusNextNavEntry` / `FocusPreviousNavEntry` | Move nav selection |
| `l` / `h` | `settings_editor::ExpandNavEntry` / `CollapseNavEntry` | Expand/collapse nav section |
| `g g` / `shift-g` | `settings_editor::FocusFirstNavEntry` / `FocusLastNavEntry` | Jump to first/last nav entry |

### Markdown preview

*Context: `MarkdownPreview`*

| Key | Action | What it does |
|---|---|---|
| `ctrl-u` / `ctrl-d` | `markdown::ScrollPageUp` / `ScrollPageDown` | Scroll by page |
| `ctrl-y` / `ctrl-e` | `markdown::ScrollUp` / `ScrollDown` | Scroll by line |

### File history view

*Context: `FileHistoryView`*

| Key | Action | What it does |
|---|---|---|
| `j` / `k` | `menu::SelectNext` / `SelectPrevious` | Move selection |
| `g g` / `shift-g` | `menu::SelectFirst` / `SelectLast` | Jump to first/last entry |

---

## Pickers & misc UI

*Context: `showing_completions`*

| Key | Action | What it does |
|---|---|---|
| `ctrl-j` / `ctrl-k` | `editor::ContextMenuNext` / `ContextMenuPrevious` | Move through completion list |

*Context: `Picker > Editor`* (search boxes, file finder, command palette input, etc.)

| Key | Action | What it does |
|---|---|---|
| `enter` | `menu::Confirm` | Confirm selection |
| `escape` | `menu::Cancel` | Close picker |
| `ctrl-u` | `editor::DeleteToBeginningOfLine` | Clear input before cursor |
| `ctrl-w` | `editor::DeleteToPreviousWordStart` | Delete previous word |
| `ctrl-k` / `up` | `menu::SelectPrevious` | Move selection up |
| `ctrl-j` / `down` | `menu::SelectNext` | Move selection down |

*Context: `BufferSearchBar && !in_replace`*

| Key | Action | What it does |
|---|---|---|
| `enter` | `vim::SearchSubmit` | Submit search |
| `escape` | `buffer_search::Dismiss` | Close search bar |

*Context: `Editor && mode == auto_height && VimControl`* (single-line inputs, e.g. commit message box)

| Key | Action | What it does |
|---|---|---|
| `/`, `?`, `#`, `*`, `n`, `shift-n` | `null` (unbound) | Search motions disabled — not yet implemented for single-line editors |

*Context: `GitCommit > Editor && VimControl && vim_mode == normal`*

| Key | Action | What it does |
|---|---|---|
| `ctrl-c` / `escape` | `menu::Cancel` | Cancel commit message |

*Context: `Editor && edit_prediction`*

| Key | Action | What it does |
|---|---|---|
| `tab` | `editor::AcceptEditPrediction` | Accept AI edit prediction (re-bound because vim's `tab` shadows it) |

*Context: `MessageEditor > Editor && VimControl`* (AI agent chat box)

| Key | Action | What it does |
|---|---|---|
| `enter` | `agent::Chat` | Send message to agent |

*Context: `os != macos && Editor && (edit_prediction && (showing_completions \|\| in_leading_whitespace))`*

| Key | Action | What it does |
|---|---|---|
| `alt-l` | `editor::AcceptEditPrediction` | Accept prediction (non-macOS fallback, since `alt-tab` is often taken by the window manager) |

*Context: `VimControl && VimCount`* (a count prefix is currently being typed)

| Key | Action | What it does |
|---|---|---|
| `0` | `vim::Number(0)` | Extra digit of the count |
| `:` | `vim::CountCommand` | Start a command with the count applied |
| `%` | `vim::GoToPercentage` | Go to N% through the file |
