import ballerina/io;

public function main() {
    decimal[] values = [9.03062786202015537577820437487338E1294];
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -9.35672041427534175678278056758842d {
        return 0;
    }
    else if val > -7.545538151437083712514877478172717E-2893d {
        return 1;
    }
    else if val > -85.2395919231473723757841289830251E-5926d {
        return 2;
    }
    return 3;
}
