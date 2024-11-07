// frontend/webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',  // React entry point
    output: {
        path: path.resolve(__dirname, 'dist'),  // Output directory
        filename: 'bundle.js',                  // Bundle file name
        publicPath: '/'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            },
            {
                test: /\.css$/,                  // For CSS files
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './public/index.html',     // HTML template
            filename: 'index.html'
        })
    ],
    devServer: {
        static: path.resolve(__dirname, 'dist'),
        historyApiFallback: true,
        port: 3000
    }
};
