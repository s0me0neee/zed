# Keymaps

Generated 2026-08-06 01:32 — 536 mappings across 13 owners.

## $VIMRUNTIME  (26)

```
n   %                                      <Plug>(MatchitNormalForward)
o   %                                      <Plug>(MatchitOperationForward)
x   %                                      <Plug>(MatchitVisualForward)
n   <Plug>(MatchitNormalBackward)          :<C-U>call matchit#Match_wrapper('',0,'n')<CR>
n   <Plug>(MatchitNormalForward)           :<C-U>call matchit#Match_wrapper('',1,'n')<CR>
n   <Plug>(MatchitNormalMultiBackward)     :<C-U>call matchit#MultiMatch("bW", "n")<CR>
n   <Plug>(MatchitNormalMultiForward)      :<C-U>call matchit#MultiMatch("W", "n")<CR>
o   <Plug>(MatchitOperationBackward)       :<C-U>call matchit#Match_wrapper('',0,'o')<CR>
o   <Plug>(MatchitOperationForward)        :<C-U>call matchit#Match_wrapper('',1,'o')<CR>
o   <Plug>(MatchitOperationMultiBackward)  :<C-U>call matchit#MultiMatch("bW", "o")<CR>
o   <Plug>(MatchitOperationMultiForward)   :<C-U>call matchit#MultiMatch("W", "o")<CR>
x   <Plug>(MatchitVisualBackward)          :<C-U>call matchit#Match_wrapper('',0,'v')<CR>m'gv``
x   <Plug>(MatchitVisualForward)           :<C-U>call matchit#Match_wrapper('',1,'v')<CR>:if col("''") != col("$") | exe ":normal! m'" | endif<CR>gv``
x   <Plug>(MatchitVisualMultiBackward)     :<C-U>call matchit#MultiMatch("bW", "n")<CR>m'gv``
x   <Plug>(MatchitVisualMultiForward)      :<C-U>call matchit#MultiMatch("W", "n")<CR>m'gv``
x   <Plug>(MatchitVisualTextObject)        <Plug>(MatchitVisualMultiBackward)o<Plug>(MatchitVisualMultiForward)
n   [%                                     <Plug>(MatchitNormalMultiBackward)
o   [%                                     <Plug>(MatchitOperationMultiBackward)
x   [%                                     <Plug>(MatchitVisualMultiBackward)
n   ]%                                     <Plug>(MatchitNormalMultiForward)
o   ]%                                     <Plug>(MatchitOperationMultiForward)
x   ]%                                     <Plug>(MatchitVisualMultiForward)
x   a%                                     <Plug>(MatchitVisualTextObject)
n   g%                                     <Plug>(MatchitNormalBackward)
o   g%                                     <Plug>(MatchitOperationBackward)
x   g%                                     <Plug>(MatchitVisualBackward)
```

## conform.nvim  (2)

```
n   <leader>cF  [lazy] Format Injected Langs
x   <leader>cF  [lazy] Format Injected Langs
```

## dial.nvim  (8)

```
n   <C-a>   [lazy] Increment
v   <C-a>   [lazy] Increment
n   <C-x>   [lazy] Decrement
v   <C-x>   [lazy] Decrement
n   g<C-a>  [lazy] Increment
x   g<C-a>  [lazy] Increment
n   g<C-x>  [lazy] Decrement
x   g<C-x>  [lazy] Decrement
```

## grug-far.nvim  (2)

```
n   <leader>sr  [lazy] Search and Replace
x   <leader>sr  [lazy] Search and Replace
```

## markdown-preview.nvim  (1)

```
n   <leader>cp  [lazy] Markdown Preview
```

## neo-tree.nvim  (6)

```
n   <leader>E   [lazy] Explorer NeoTree (cwd)
n   <leader>be  [lazy] Buffer Explorer
n   <leader>e   [lazy] Explorer NeoTree (Root Dir)
n   <leader>fE  [lazy] Explorer NeoTree (cwd)
n   <leader>fe  [lazy] Explorer NeoTree (Root Dir)
n   <leader>ge  [lazy] Git Explorer
```

## nvim-dap  (17)

```
n   <leader>dB  [lazy] Breakpoint Condition
n   <leader>dC  [lazy] Run to Cursor
n   <leader>dO  [lazy] Step Over
n   <leader>dP  [lazy] Pause
n   <leader>da  [lazy] Run with Args
n   <leader>db  [lazy] Toggle Breakpoint
n   <leader>dc  [lazy] Run/Continue
n   <leader>dg  [lazy] Go to Line (No Execute)
n   <leader>di  [lazy] Step Into
n   <leader>dj  [lazy] Down
n   <leader>dk  [lazy] Up
n   <leader>dl  [lazy] Run Last
n   <leader>do  [lazy] Step Out
n   <leader>dr  [lazy] Toggle REPL
n   <leader>ds  [lazy] Session
n   <leader>dt  [lazy] Terminate
n   <leader>dw  [lazy] Widgets
```

## nvim-dap-python  (2)

```
n   <leader>dPc  [lazy] Debug Class
n   <leader>dPt  [lazy] Debug Method
```

## nvim-dap-ui  (3)

```
n   <leader>de  [lazy] Eval
x   <leader>de  [lazy] Eval
n   <leader>du  [lazy] Dap UI
```

## triforce.nvim  (1)

```
n   <leader>T  [lazy] 
```

## unknown (vimscript / :map)  (96)

```
n    cA         Source Action
n    cC         Refresh & Display Codelens
n    cR         Rename File
n    ca         Code Action
x    ca         Code Action
n    cc         Run Codelens
x    cc         Run Codelens
n    cl         Lsp Info
n    cr         Rename (inc-rename.nvim)
n    ghB        Blame Buffer
n    ghD        Diff This ~
n    ghR        Reset Buffer
n    ghS        Stage Buffer
n    ghb        Blame Line
n    ghd        Diff This
n    ghp        Preview Hunk Inline
n    ghr        Reset Hunk
x    ghr        Reset Hunk
n    ghs        Stage Hunk
x    ghs        Stage Hunk
n    ghu        Undo Stage Hunk
n    sS         LSP Workspace Symbols
n    ss         LSP Symbols
n    um         Toggle Render Markdown
x   #           :help v_#-default
n   &           :help &-default
x   *           :help v_star-default
c   <C-R>       which-key-trigger registers
i   <C-U>       :help i_CTRL-U-default
i   <C-W>       :help i_CTRL-W-default
n   <C-W><C-D>  Show diagnostics under the cursor
n   <C-W>d      Show diagnostics under the cursor
n   <M-n>       Next Reference
n   <M-p>       Prev Reference
i   <S-Tab>     vim.snippet.jump if active, otherwise <S-Tab>
s   <S-Tab>     vim.snippet.jump if active, otherwise <S-Tab>
i   <Tab>       vim.snippet.jump if active, otherwise <Tab>
s   <Tab>       vim.snippet.jump if active, otherwise <Tab>
x   @           :help v_@-default
n   K           Hover
x   Q           :help v_Q-default
n   Y           :help Y-default
n   [           Add empty line above cursor
n   [<C-L>      :lpfile
n   [<C-Q>      :cpfile
n   [<C-T>      :ptprevious
n   [A          :rewind
n   [D          Jump to the first diagnostic in the current buffer
n   [H          First Hunk
n   [L          :lrewind
x   [N          Select previous sibling node
n   [Q          :crewind
n   [T          :trewind
n   [[          Prev Reference
n   [a          :previous
n   [h          Prev Hunk
n   [l          :lprevious
x   [n          Select previous node
n   ]           Add empty line below cursor
n   ]<C-L>      :lnfile
n   ]<C-Q>      :cnfile
n   ]<C-T>      :ptnext
n   ]A          :last
n   ]D          Jump to the last diagnostic in the current buffer
n   ]H          Last Hunk
n   ]L          :llast
x   ]N          Select next sibling node
n   ]Q          :clast
n   ]T          :tlast
n   ]]          Next Reference
n   ]a          :next
n   ]h          Next Hunk
n   ]l          :lnext
x   ]n          Select next node
n   gD          Goto Declaration
n   gI          Goto Implementation
n   gK          Signature Help
n   gO          vim.lsp.buf.document_symbol()
n   gc          Toggle comment
o   gc          Comment textobject
x   gc          Toggle comment
n   gcc         Toggle comment line
n   gd          Goto Definition
n   gr          References
n   gra         vim.lsp.buf.code_action()
x   gra         vim.lsp.buf.code_action()
n   gri         vim.lsp.buf.implementation()
n   grn         vim.lsp.buf.rename()
n   grr         vim.lsp.buf.references()
n   grt         vim.lsp.buf.type_definition()
n   grx         vim.lsp.codelens.run()
n   gx          Opens filepath or URI under cursor with the system handler (file explorer, web browser, …)
x   gx          Opens filepath or URI under cursor with the system handler (file explorer, web browser, …)
n   gy          Goto T[y]pe Definition
o   ih          GitSigns Select Hunk
x   ih          GitSigns Select Hunk
```

## user config  (371)

```
n                Find Files (Root Dir)
n    ,           Buffers
n    -           Split Window Below
n    .           Toggle Scratch Buffer
n    /           Grep (Root Dir)
n    :           Command History
n    <Tab><Tab>  New Tab
n    <Tab>[      Previous Tab
n    <Tab>]      Next Tab
n    <Tab>d      Close Tab
n    <Tab>f      First Tab
n    <Tab>l      Last Tab
n    <Tab>o      Close Other Tabs
n    ?           Buffer Keymaps (which-key)
n    E           Explorer NeoTree (cwd)
n    K           Keywordprg
n    L           LazyVim Changelog
n    S           Select Scratch Buffer
n    T           <lua callback>
n    `           Switch to Other Buffer
n    bD          Delete Buffer and Window
n    bP          Delete Non-Pinned Buffers
n    bb          Switch to Other Buffer
n    bd          Delete Buffer
n    be          Buffer Explorer
n    bi          Delete Invisible Buffers
n    bj          Pick Buffer
n    bl          Delete Buffers to the Left
n    bo          Delete Other Buffers
n    bp          Toggle Pin
n    br          Delete Buffers to the Right
n    cF          Format Injected Langs
x    cF          Format Injected Langs
n    cG          Toggle Claude Code
n    cS          LSP references/definitions/... (Trouble)
n    cd          Line Diagnostics
n    cf          Format
x    cf          Format
n    cm          Mason
n    cq          Color pick under cursor
n    cs          Symbols (Trouble)
n    dB          Breakpoint Condition
n    dC          Run to Cursor
n    dO          Step Over
n    dP          Pause
n    da          Run with Args
n    db          Toggle Breakpoint
n    dc          Run/Continue
n    de          Eval
x    de          Eval
n    dg          Go to Line (No Execute)
n    di          Step Into
n    dj          Down
n    dk          Up
n    dl          Run Last
n    do          Step Out
n    dph         Toggle Profiler Highlights
n    dpp         Toggle Profiler
n    dps         Profiler Scratch Buffer
n    dr          Toggle REPL
n    ds          Session
n    dt          Terminate
n    du          Dap UI
n    dw          Widgets
n    e           Explorer NeoTree (Root Dir)
n    fB          Buffers (all)
n    fE          Explorer NeoTree (cwd)
n    fF          Find Files (cwd)
n    fR          Recent (cwd)
n    fT          Terminal (cwd)
n    fb          Buffers
n    fc          Find Config File
n    fe          Explorer NeoTree (Root Dir)
n    ff          Find Files (Root Dir)
n    fg          Find Files (git-files)
n    fn          New File
n    fp          Projects
n    fr          Recent
n    ft          Terminal (Root Dir)
n    gB          Git Browse (open)
x    gB          Git Browse (open)
n    gD          Git Diff (origin)
n    gG          Lazygit (cwd)
n    gI          GitHub Issues (all)
n    gL          Git Log (cwd)
n    gP          GitHub Pull Requests (all)
n    gS          Git Stash
n    gY          Git Browse (copy)
x    gY          Git Browse (copy)
n    gb          Git Blame Line
n    gd          Git Diff (hunks)
n    ge          Git Explorer
n    gf          Git Current File History
n    gg          Lazygit (Root Dir)
n    gi          GitHub Issues (open)
n    gl          Git Log
n    gp          GitHub Pull Requests (open)
n    gs          Git Status
n    h           Dashboard
n    l           Lazy
n    n           Notification History
n    qS          Select Session
n    qd          Don't Save Current Session
n    ql          Restore Last Session
n    qq          Quit All
n    qs          Restore Session
n    s"          Registers
n    s/          Search History
n    sB          Grep Open Buffers
n    sC          Commands
n    sD          Buffer Diagnostics
n    sG          Grep (cwd)
n    sH          Highlights
n    sM          Man Pages
n    sR          Resume
n    sT          Todo/Fix/Fixme
n    sW          Visual selection or word (cwd)
x    sW          Visual selection or word (cwd)
n    sa          Autocmds
n    sb          Buffer Lines
n    sc          Command History
n    sd          Diagnostics
n    sg          Grep (Root Dir)
n    sh          Help Pages
n    si          Icons
n    sj          Jumps
n    sk          Keymaps
n    sl          Location List
n    sm          Marks
n    sn          +noice
n    sna         Noice All
n    snd         Dismiss All
n    snh         Noice History
n    snl         Noice Last Message
n    snt         Noice Picker (Telescope/FzfLua)
n    sp          Search for Plugin Spec
n    sq          Quickfix List
n    sr          Search and Replace
x    sr          Search and Replace
n    st          Todo
n    su          Undotree
n    sw          Visual selection or word (Root Dir)
x    sw          Visual selection or word (Root Dir)
n    t            Themes
n    uA          Toggle Tabline
n    uC          Colorschemes
n    uD          Toggle Dimming
n    uF          Toggle Auto Format (Buffer)
n    uG          Toggle Git Signs
n    uI          Inspect Tree
n    uL          Toggle Relative Number
n    uS          Toggle Smooth Scroll
n    uT          Toggle Treesitter Highlight
n    uU          Enable theme transparency
n    uZ          Toggle Zoom Mode
n    ua          Toggle Animations
n    ub          Toggle Dark Background
n    uc          Toggle Conceal Level
n    ud          Toggle Diagnostics
n    uf          Toggle Auto Format (Global)
n    ug          Toggle Indent Guides
n    uh          Toggle Inlay Hints
n    ui          Inspect Pos
n    ul          Toggle Line Numbers
n    un          Dismiss All Notifications
n    up          Toggle Mini Pairs
n    ur          Redraw / Clear hlsearch / Diff Update
n    us          Toggle Spelling
n    uw          Toggle Wrap
n    uz          Toggle Zen Mode
n    wd          Delete Window
n    wm          Toggle Zoom Mode
n    xL          Location List (Trouble)
n    xQ          Quickfix List (Trouble)
n    xT          Todo/Fix/Fixme (Trouble)
n    xX          Buffer Diagnostics (Trouble)
n    xl          Location List
n    xq          Quickfix List
n    xt          Todo (Trouble)
n    xx          Diagnostics (Trouble)
n    |           Split Window Right
c   "            Closeopen action for '""' pair
i   "            Closeopen action for '""' pair
c   '            Closeopen action for "''" pair
i   '            Closeopen action for "''" pair
c   (            Open action for "()" pair
i   (            Open action for "()" pair
c   )            Close action for "()" pair
i   )            Close action for "()" pair
i   ,            ,<C-G>u
n   ,            <lua callback>
o   ,            <lua callback>
x   ,            <lua callback>
i   .            .<C-G>u
i   ;            ;<C-G>u
n   ;            <lua callback>
o   ;            <lua callback>
x   ;            <lua callback>
c   <BS>         MiniPairs <BS>
i   <BS>         MiniPairs <BS>
n   <C-/>        Terminal (Root Dir)
t   <C-/>        Terminal (Root Dir)
n   <C-A>        Increment
s   <C-A>        Increment
x   <C-A>        Increment
i   <C-B>        Scroll Backward
n   <C-B>        Scroll Backward
s   <C-B>        Scroll Backward
n   <C-Down>     Decrease Window Height
i   <C-F>        Scroll Forward
n   <C-F>        Scroll Forward
s   <C-F>        Scroll Forward
n   <C-H>        Go to Left Window
n   <C-J>        Go to Lower Window
n   <C-K>        Go to Upper Window
n   <C-L>        Go to Right Window
n   <C-Left>     Decrease Window Width
n   <C-Right>    Increase Window Width
c   <C-S>        Toggle Flash Search
i   <C-S>        Save File
n   <C-S>        Save File
s   <C-S>        Save File
x   <C-S>        Save File
n   <C-Space>    Treesitter Incremental Selection
o   <C-Space>    Treesitter Incremental Selection
x   <C-Space>    Treesitter Incremental Selection
n   <C-Up>       Increase Window Height
n   <C-W>        Window Hydra Mode (which-key)
n   <C-X>        Decrement
s   <C-X>        Decrement
x   <C-X>        Decrement
n   <C-_>        which_key_ignore
t   <C-_>        which_key_ignore
i   <CR>         MiniPairs <CR>
n   <Down>       Down
x   <Down>       Down
i   <Esc>        Escape and Clear hlsearch
n   <Esc>        Escape and Clear hlsearch
s   <Esc>        Escape and Clear hlsearch
i   <M-j>        Move Down
n   <M-j>        Move Down
s   <M-j>        Move Down
x   <M-j>        Move Down
i   <M-k>        Move Up
n   <M-k>        Move Up
s   <M-k>        Move Up
x   <M-k>        Move Up
c   <S-CR>       Redirect Cmdline
n   <Up>         Up
x   <Up>         Up
x   <lt>         <lt>gv
x   >            >gv
n   F            <lua callback>
o   F            <lua callback>
x   F            <lua callback>
n   H            Prev Buffer
n   L            Next Buffer
n   N            Prev Search Result
o   N            Prev Search Result
x   N            Prev Search Result
o   R            Treesitter Search
x   R            Treesitter Search
n   S            Flash Treesitter
o   S            Flash Treesitter
x   S            Flash Treesitter
n   T            <lua callback>
o   T            <lua callback>
x   T            <lua callback>
c   [            Open action for "[]" pair
i   [            Open action for "[]" pair
n   [A           Prev Parameter End
o   [A           Prev Parameter End
x   [A           Prev Parameter End
n   [B           Move buffer prev
n   [C           Prev Class End
o   [C           Prev Class End
x   [C           Prev Class End
n   [F           Prev Function End
o   [F           Prev Function End
x   [F           Prev Function End
n   [a           Prev Parameter Start
o   [a           Prev Parameter Start
x   [a           Prev Parameter Start
n   [b           Prev Buffer
n   [c           Prev Class Start
o   [c           Prev Class Start
x   [c           Prev Class Start
n   [d           Prev Diagnostic
n   [e           Prev Error
n   [f           Prev Function Start
o   [f           Prev Function Start
x   [f           Prev Function Start
n   [q           Previous Trouble/Quickfix Item
n   [t           Previous Todo Comment
n   [w           Prev Warning
n   \r           Run Lua
x   \r           Run Lua
c   ]            Close action for "[]" pair
i   ]            Close action for "[]" pair
n   ]A           Next Parameter End
o   ]A           Next Parameter End
x   ]A           Next Parameter End
n   ]B           Move buffer next
n   ]C           Next Class End
o   ]C           Next Class End
x   ]C           Next Class End
n   ]F           Next Function End
o   ]F           Next Function End
x   ]F           Next Function End
n   ]a           Next Parameter Start
o   ]a           Next Parameter Start
x   ]a           Next Parameter Start
n   ]b           Next Buffer
n   ]c           Next Class Start
o   ]c           Next Class Start
x   ]c           Next Class Start
n   ]d           Next Diagnostic
n   ]e           Next Error
n   ]f           Next Function Start
o   ]f           Next Function Start
x   ]f           Next Function Start
n   ]q           Next Trouble/Quickfix Item
n   ]t           Next Todo Comment
n   ]w           Next Warning
c   `            Closeopen action for "``" pair
i   `            Closeopen action for "``" pair
o   a            Around textobject
x   a            Around textobject
o   al           Around last textobject
x   al           Around last textobject
o   an           Around next textobject
x   an           Around next textobject
n   f            <lua callback>
o   f            <lua callback>
x   f            <lua callback>
n   g<C-A>       Increment
x   g<C-A>       Increment
n   g<C-X>       Decrement
x   g<C-X>       Decrement
n   g[           Move to left "around"
o   g[           Move to left "around"
x   g[           Move to left "around"
n   g]           Move to right "around"
o   g]           Move to right "around"
x   g]           Move to right "around"
n   gcO          Add Comment Above
n   gco          Add Comment Below
o   i            Inside textobject
x   i            Inside textobject
o   il           Inside last textobject
x   il           Inside last textobject
o   in           Inside next textobject
x   in           Inside next textobject
n   j            Down
x   j            Down
n   k            Up
x   k            Up
n   n            Next Search Result
o   n            Next Search Result
x   n            Next Search Result
o   r            Remote Flash
n   s            Flash
o   s            Flash
x   s            Flash
n   t            <lua callback>
o   t            <lua callback>
x   t            <lua callback>
c   {            Open action for "{}" pair
i   {            Open action for "{}" pair
c   }            Close action for "{}" pair
i   }            Close action for "{}" pair
```

## venv-selector.nvim  (1)

```
n   <leader>cv  [lazy] Select VirtualEnv
```

