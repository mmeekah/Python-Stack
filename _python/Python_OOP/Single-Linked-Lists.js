const util = require("util");
class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

class List {
  constructor(head = null) {
    this.head = head;
  }
  printAll() {
    var runner = this.head;
    if (runner == null) {
      console.log(runner);
      return;
    }
    while (runner.next != null) {
      console.log(runner.val);
      runner = runner.next;
    }
    console.log(runner.val);
  }
  addToBack(val) {
    var runner = this.head;
    while (runner.next != null) {
      runner = runner.next;
    }
    runner.next = new Node(val);
    return runner.next;
  }
  addToFront(val) {
    var newhead = new Node(val);
    var original = this.head;

    if (this.head != null) {
      this.head = newhead;
      newhead.next = original;
    } else {
      this.head = newhead;
    }
  }
  removeFromFront() {
    var original = this.head;
    var newLinkedList = this.head.next;
    original.next = null;
    this.head = newLinkedList;
  }
  addAtAnIndex(val, index) {
    var check = 0;
    var firstPart = this.head;
    while (check < index - 1) {
      firstPart = firstPart.next;
      check++;
    }
    var secondPart = firstPart.next;
    var val = new Node(val);
    firstPart.next = val;
    val.next = secondPart;
  }
  contain(value) {
    var runner = this.head;
    if (this.head == nul)
      while (runner.next != value) {
        if (runner.val == value) {
          return true;
        } else {
          runner = runner.next;
        }
      }
    if (runner.val == value) {
      return true;
    } else {
      return false;
    }
  }
  removeBack() {
    var runner = this.head;
    if (runner != null) {
      if (runner.next == null) {
        this.head = null;
      } else {
        while (runner.next.next != null) {
          runner = runner.next;
        }
        runner.next = null;
      }
    }
  }
  // removeBack(){
  //   var runner = this.head.next;
  //   var prevRunner = this.head;
  //   if (runner == null){
  //     this.head = null;
  //   }
  //   else{
  //     while (runner.next != null){
  //       prevRunner = runner;
  //       runner = runner.next;
  //     }
  //     prevRunner.next = null;
  //   }
  // }
  minimumToFront() {
    if (this.head == null) {
      return false;
    }
    if (this.head.next == null) {
      return this.head;
    } else {
      var movingNode = this.head;
      var runner = this.head;
      var min = this.head.val;
      var previous = this.head;

      while (runner.next != null) {
        if (runner.next.val < min) {
          previous = runner;
          min = runner.val;
          movingNode = runner.next;
          console.log("the minimum is" + min);
        }
        runner = runner.next;
      }
      movingNode.next = this.head;
      this.head = movingNode;
      previous.next = null;
      return movingNode;
    }
  }
  removeThatNode(value) {
    if (this.head == null) {
      return false;
    } else if (this.head.next == null) {
      if (this.head.val == value) {
        var previous = this.head;
        this.head = null;
        return previous;
      }
    } else {
      var nextnode = this.head;
      var runner = this.head;
      var previous = this.head;

      while (runner.next != null) {
        if (runner.next.val == value) {
          nextnode = runner.next.next;
          previous = runner;
        }
        runner = runner.next;
      }
      previous.next = nextnode;
    }
  }
  secondToLast() {
    if (this.head == null) {
      return false;
    } else if (this.head.next == null) {
      return false;
    } else {
      var runner = this.head;
      while (runner.next.next != null) {
        runner = runner.next;
      }
      var secondlast = runner.val;
      return secondlast;
    }
  }
  concatlist(list2) {
    var runner = this.head;
    while (runner.next != null) {
      runner = runner.next;
    }
    runner.next = list2.head;
  }
  partition(value) {
    var runner = this.head;

    while (runner != null) {
      if (runner.val > value) {
        this.removeThatNode(runner.val);
        this.addToBack(runner.val);
      } else if (runner.val < value) {
        this.removeThatNode(runner.val);
        this.addToFront(runner.val);
      } else {
      }
      runner = runner.next;
    }
  }
  reverse() {
    console.log("Starting Reverse Method");
    if (!this.head || !this.head.next) return this;
    let first = this.head;
    console.log("First: " + JSON.stringify(first));
    while (first.next) {
      const newHead = first.next;
      // cut the newHead out from where it current is
      first.next = first.next.next;
      newHead.next = this.head;
      this.head = newHead;
      console.log("List: " + JSON.stringify(this.head));
    }
    return this;
  }
  hasLoop() {
    if (!this.head || !this.head.next) return false;
    let runner = this.head;
    let runner2 = runner.next;
    let count = 0
    console.log("Runner is: ", runner);
    console.log("Runner2 is: ", runner2);
    while (runner2.next != null && runner2.next.next != null) {
      count++;
      runner = runner.next;
      runner2 = runner2.next.next;
      if (runner == runner2) {
        return true;
      }
    }
    console.log("Count is: ", count)
    return false;
  }
}

var tumbler = new List();
var forty = new Node(40);
tumbler.head = forty;
tumbler.addToBack(30);
tumbler.addToBack(20);
tumbler.addToBack(10);
tumbler.addToBack(50);
tumbler.addToBack(60);
tumbler.addToBack(70);
const lastNode = tumbler.addToBack(80);
lastNode.next = tumbler.head
console.log(util.inspect(tumbler, { showHidden: false, depth: null }))
// tumbler.partition(20);
// tumbler.printAll();
// var list2 = new List();
// var fifty = new Node(50);
// list2.head = fifty;
// list2.addToBack(60);
// list2.addToBack(70);
// list2.addToBack(80);

// tumbler.reverse();
// tumbler.printAll();
console.log(tumbler.hasLoop());
