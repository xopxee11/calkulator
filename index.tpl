<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>My calc</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="icon" href="icon.ico">
</head>
<body>
    <div id="wrapper">
        <form action="/" method="POST">
            %if result == 'error':
                <input id="input" name="expression" type="text" autofocus placeholder="Only 1234567890 + - * / // % ** ()">
            %elif result is not None:
                <input id="input" name="expression" type="text" autofocus placeholder="{{ result }}">
            %else:
                <input id="input" name="expression" type="text" autofocus placeholder="Type your expression here and push 'Get result'">
            %end
            <input id="btn" value="Get result" type="submit">
        </form>
    </div>
</body>
</html>