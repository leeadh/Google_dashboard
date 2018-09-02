var config = {};

config.mongodb = {};
config.server = {};

config.server.port = process.env.WEB_PORT || 9999;

config.mongodb.username = process.env.MONGODB_USERNAME || 'leexha';
config.mongodb.password=  process.env.MONGODB_PASSWORD || 'Password123_!';
config.mongodb.host=  process.env.MONGODB_HOST || '54.255.141.174';
config.mongodb.port = process.env.MONGODB_PORT || 27017;
config.mongodb.databaseName = process.env.MONGODB_NAME || 'DATA_DB';

module.exports = config;
