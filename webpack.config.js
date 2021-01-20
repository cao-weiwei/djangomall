var path = require('path'),
    webpack = require('webpack'),
    BundleTracker = require('webpack-bundle-tracker'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    context: __dirname,
    entry: [
        './static/js/index',
        './static/css/base.css'
    ],
    output: {
        path: path.resolve('./static/webpack_bundles/'),
        filename: '[name].js',
    },
    module: {
        rules: [
            // 增加 JSX 的处理
            {
                test: /\.(js|jsx)$/,
                resolve: {
                    extensions: ['.js', '.jsx'],
                },
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            // 增加 CSS 的处理
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
            // 增加对图片、字体等文件的处理
            {
                test: /\.(jpg|png|svg|ttf|woff|woff2|eot)\??.*$/,
                use: ['url-loader']
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader'],
            },
        ]
    },
    plugins: [
        new MiniCssExtractPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})
    ],
};
