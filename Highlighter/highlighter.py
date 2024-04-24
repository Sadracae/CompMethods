import re 

def syntax_highlight(text):
    # Color styles for syntax highlighting
    colors = {
        'operator': 'color: #0000FF;',  # Blue
        'comment': 'color: #008000;',   # Green
        'string': 'color: #9C27B0;',    # Purple
        'integer': 'color: #F9A825;',   # Yellow
        'assign_operator': 'color: #B6F542;',  # Light green
        'keyword': 'color: #D32F2F;',  # Red
    }

    # Regular expression patterns for different syntax elements
    syntax_patterns = {
        'operator': (r'[\+\-\*\/<>=]', colors['operator']),
        'comment': (r'\/\/.*|\/\*[\s\S]*?\*\/|#.*', colors['comment']),
        'string': (r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\'', colors['string']),
        'integer': (r'\b\d+\b', colors['integer']),
        'assign_operator': (r'[+\-\*/]?=', colors['assign_operator']),
        'keyword': (r'if|else|for|while|def', colors['keyword']),
    }
  
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, (pattern, _) in syntax_patterns.items())

    # Function to apply styles to matched syntax elements
    def style_replacer(match):
        for name, style in colors.items():
            value = match.group(name)
            if value:
                return f'<span style="{style}">{value}</span>'
        return match.group(0)

    # Applying syntax highlighting to the text
    highlighted_text = re.sub(combined_pattern, style_replacer, text, flags=re.MULTILINE)
    return highlighted_text

# Read code from a file
with open('code.txt', 'r') as file:
    code_text = file.read()

# Highlight the syntax in the code
highlighted_code = syntax_highlight(code_text)

# Generate HTML output with highlighted code
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Syntax Highlighted Code</title>
</head>
<body>
<pre>{highlighted_code}</pre>
</body>
</html>
"""

# Write the HTML output to a file
with open('highlighted_code.html', 'w') as file:
    file.write(html_output)
