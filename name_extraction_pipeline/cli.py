import sys
import json
from name_extraction_pipeline.dispatcher import extract_first_name

def main():
    if len(sys.argv) != 2:
        print("Usage: namedropper <full_name>")
        sys.exit(1)

    full_name = sys.argv[1]
    result = extract_first_name(full_name)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
