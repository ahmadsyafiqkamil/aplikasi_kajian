import React from 'react';
import ReactDOM from 'react-dom';

function MyApp() {
    return (
        <div>
            <h1>Hello World!</h1>
        </div>
    );
}

ReactDOM.render(
    <MyApp/>,
    document.getElementById('root')
);

export default MyApp;

