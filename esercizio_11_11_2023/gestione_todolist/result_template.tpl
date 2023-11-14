<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Query Results</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Query Results</h2>
    <table>
        <tbody>
            % for row in result:
                <tr>
                    % for value in row:
                        <td>{{value}}</td>
                    % end
                </tr>
            % end
        </tbody>
    </table>
</body>
</html>