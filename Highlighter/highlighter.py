import re 

def highlight_code(text):
    # Styles
    styles = {
        'operator': 'color: #0000FF;',
        'comment': 'color: #E64E29;',
        'string': 'color: #9C27B0;',
        'integer': 'color: #F9A825;',
        'assign_operator': 'color: #689F38;',
        'keyword': 'color: #D32F2F;',
        
    }

    # Identifiers
    patterns = {
        'operator': (r'[\+\-\*\/<>=]', styles['operator']),
        'comment': (r'\/\/.*|\/\*[\s\S]*?\*\/|#.*', styles['comment']),
        'string': (r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\'', styles['string']),
        'integer': (r'\b\d+\b', styles['integer']),
        'assign_operator': (r'[+\-\*/]?=', styles['assign_operator']),
        'keyword': (r'if|else|for|while', styles['keyword']),
        
    }
  
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, (pattern, _) in patterns.items())

    
    def style_replacer(match):
        for name, style in styles.items():
            value = match.group(name)
            if value:
                return f'<span style="{style}">{value}</span>'
        return match.group(0)


    highlighted_code = re.sub(combined_pattern, style_replacer, text, flags=re.MULTILINE)
    return highlighted_code

with open('code.txt', 'r') as file:
    text = file.read()


highlighted_code = highlight_code(text)


html_out = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Code Highlighter</title>
</head>
<body>
<pre>{highlighted_code}</pre>
</body>
</html>
"""

with open('out.html', 'w') as file:
    file.write(html_out)