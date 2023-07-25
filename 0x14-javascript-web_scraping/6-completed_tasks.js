#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const todos = JSON.parse(body);
  const completed = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (completed[todo.userId]) {
        completed[todo.userId] += 1;
      } else {
        completed[todo.userId] = 1;
      }
    }
  }
  for (const [user, count] of Object.entries(completed)) {
    console.log(`User ${user} has completed ${count} tasks`);
  }
});
