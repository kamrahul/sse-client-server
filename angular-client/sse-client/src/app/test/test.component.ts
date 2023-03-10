import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.sass']
})
export class TestComponent implements OnInit {

  myData: any;
  constructor() { }

  ngOnInit(): void {
    this.connect();
  }

  connect(): void {
    let source = new EventSource('http://localhost:7001/stream');
    source.addEventListener('message', message => {
        this.myData = message.data; 
        console.log(message.data)       
    });
 }

}
