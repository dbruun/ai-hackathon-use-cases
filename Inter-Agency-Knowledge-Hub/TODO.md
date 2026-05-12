# Inter-Agency Knowledge Hub - TODO

## UI
- [ ] Add static/index.html with search interface
- [ ] Search box with query input
- [ ] Agency filter checkboxes (DMV, DOL, OTDA, DOH, OGS)
- [ ] Auth role selector (admin, staff, public) using mock tokens
- [ ] Results list with citations and permission badges
- [ ] Add static/styles.css
- [ ] Add static/search.js
- [ ] Wire up Flask to serve static files at /

## Bug Fixes
- [x] Fix DocumentClassification string vs enum in permission_filter (search_service.py)
- [x] Install flask[async] dependency

## Future
- [ ] Add real Foundry agent for semantic search summarization
