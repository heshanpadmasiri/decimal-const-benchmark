import ballerina/io;

public function main() {
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -7003164506.917643701719419601590980E4734d {
        return 0;
    }
    else if val > -7394176110242.295401276139855383536E1657d {
        return 1;
    }
    else if val > -96925.79999754536946299773849691693d {
        return 2;
    }
    else if val > -425545163011269759690.3373141778027E-1855d {
        return 3;
    }
    else if val > -7520.678144000789817339850852395559E-4985d {
        return 4;
    }
    else if val > 906800420906056.406985117092212149E-3612d {
        return 5;
    }
    else if val > 2.611485733737712154716106212051169d {
        return 6;
    }
    else if val > 2684253.249076473867486978112186425d {
        return 7;
    }
    else if val > 921386189671817236.408554846781634d {
        return 8;
    }
    else if val > 48227234414385549648.05906081160949d {
        return 9;
    }
    return 10;
}