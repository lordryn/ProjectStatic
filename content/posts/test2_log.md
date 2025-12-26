## [Checkpoint] Dashboard Auto-Refresh Enabled

**Date:** 2025-07-03  
**Author:** Ryn (WCS)  
**Component:** Jump Server → Frontend (`base.html`)

### :white_check_mark: Summary
Added a 30-second **full page auto-refresh** to the dashboard to ensure:
- Device statuses (`Online`, `Offline`, etc.)
- Notification bell contents  
...remain in sync without requiring manual reloads.

This is a **temporary but effective measure** during early-phase development before implementing async updates or WebSocket-based updates.

### :tools: Changes Made
- Injected a simple JavaScript `setInterval()` to reload the page every 30 seconds.
- Countdown timer text (`Refreshing in Xs`) added for admin UX clarity.

### :file_folder: Files Modified
- `templates/base.html`

### :lock: Notes
This approach trades efficiency for simplicity—acceptable during MVP stage. Will be revisited later when we integrate:
- Fragment-based partial refreshes
- Notification polling or socket triggers
- Client-driven "ping" or status update triggers

---