### Debug
This command searches for the term 'traceloop.sdk' within files and extracts the repository full names using jq
```
python3 ./code_search.py 'traceloop.sdk+in:file'   | jq -r '.items[].repository.full_name'
```
