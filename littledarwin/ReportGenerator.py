from builtins import str
from builtins import range
from builtins import object
import os
import shelve

__author__ = 'APSXR'


class ReportGenerator(object):
    def __init__(self):
        self.database = None

    def initiateDatabase(self, databasePath):
        self.database = shelve.open(databasePath, "c")

    def generateHTMLFinalReport(self, resultData, reportPath):
        reportBeginning = """
            <html>
            <head>

            <style type='text/css'>
            table {
                border-collapse: collapse;
            }

            table, th, td {
                border: 2px solid black;
            }

            .tests{
                width : 50%;
                float : left;
            }

            .mutees{
                float : right;
                width : 50%;
            }

            .unit {
                padding-top : 20px;
                clear : both;
            }

            .coverage_bar {
                display : inline-block;
                height : 1.1em;
                width: 130px;
                background: #F55;
                margin: 0 5px;
                vertical-align: middle;
                border: 1px solid #888;
                position : relative;
            }

            .coverage_complete {
                display : inline-block;
                height : 100%;
                background: #5F5;
                float: left;
            }

            .coverage_legend {
                position : absolute;
                height : 100%;
                width : 100%;
                left : 0;
                top : 0;
                text-align : center;
            }

            .line, .mut {
                vertical-align : middle;
            }

            .coveragePercentage {
                display: inline-block;
                width: 3em;
                text-align: right;
            }
        </style>
        </head>
        <body>
            <h1>LittleDarwin Mutation Coverage Report</h1>
            <h3>Project Summary</h3>
            <table>
                <thead>
                    <tr>
                        <th>Number of Files</th>
                        <th colspan=2 >Mutation Coverage</th>
                    </tr>
                </thead>
                <tbody>

        """

        reportMiddle = """
                </tbody>
            </table>
            <h3>Breakdown by File</h3>
            <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th colspan=2 >Mutation Coverage</th>
                </tr>
            </thead>
            <tbody>


        """

        reportEnd = """
            </tbody>
        </table>
        <br/>
        <hr/> Report generated by LittleDarwin 0.4
        </body>
        </html>
        """

        totalMutantCount = 0
        survivedMutantCount = 0
        breakdownFile = list()

        for mutationResult in resultData:
            survivedMutantCount += mutationResult[1]
            totalMutantCount += mutationResult[2]
            breakdownFile.append("<tr><td><a href=\"" + os.path.relpath(
                os.path.join(os.path.dirname(reportPath), mutationResult[0], "results.html"),
                os.path.dirname(reportPath)) + "\" >" + os.path.relpath(
                os.path.join(os.path.dirname(reportPath), mutationResult[0]),
                os.path.dirname(reportPath)) + "</a></td> <td> " + ("%3.1f" % (
                100 - (mutationResult[1] / float(mutationResult[
                                                     2]) * 100))) + " </td> <td> <div class=\"coverage_bar\"><div class=\"coverage_complete\" style=\"width:" + (
                                     "%d" % (100 - (mutationResult[1] / float(
                                         mutationResult[
                                             2]) * 100))) + "%\"></div><div class=\"coverage_legend\">" + str(
                mutationResult[2] - mutationResult[1]) + "/" + str(mutationResult[2]) + "</div></div></td></tr>")

        killedMutantCount = totalMutantCount - survivedMutantCount

        projectOverallStats = "<tr><td>" + str(len(resultData)) + " </td> <td> " + ("%3.1f" % (float(
            killedMutantCount) / totalMutantCount * 100)) + " </td> <td> <div class=\"coverage_bar\"><div class=\"coverage_complete\" style=\"width:" + (
                                  "%d" % (float(
                                      killedMutantCount) / totalMutantCount * 100)) + "%\"></div><div class=\"coverage_legend\">" + str(
            killedMutantCount) + "/" + str(totalMutantCount) + "</div></div></td></tr>"

        reportOutput = list()
        reportOutput.extend([reportBeginning, projectOverallStats, reportMiddle])
        reportOutput.extend(breakdownFile)
        reportOutput.append(reportEnd)

        return '\n'.join(reportOutput)

    def generateHTMLReportPerFile(self, filePath, reportPath, survived, killed):
        def xstr(inputVar):
            if inputVar is None:
                return ''
            else:
                return str(inputVar)

        self.database[filePath] = (survived, killed)

        reportBeginning = """
            <html>
            <head>

            <style type='text/css'>
            table {
                border-collapse: collapse;
            }

            table, th, td {
                border: 2px solid black;
            }

            .tests{
                width : 50%;
                float : left;
            }

            .mutees{
                float : right;
                width : 50%;
            }

            .unit {
                padding-top : 20px;
                clear : both;
            }

            .coverage_bar {
                display : inline-block;
                height : 1.1em;
                width: 130px;
                background: #F55;
                margin: 0 5px;
                vertical-align: middle;
                border: 1px solid #888;
                position : relative;
            }

            .coverage_complete {
                display : inline-block;
                height : 100%;
                background: #5F5;
                float: left;
            }

            .coverage_legend {
                position : absolute;
                height : 100%;
                width : 100%;
                left : 0;
                top : 0;
                text-align : center;
            }

            .line, .mut {
                vertical-align : middle;
            }

            .coveragePercentage {
                display: inline-block;
                width: 3em;
                text-align: right;
            }
        </style>
        </head>
        <body>
            <h1>LittleDarwin Mutation Coverage Report</h1>
            <h3>File Summary</h3>
            <table>
                <thead>
                    <tr>
                        <th>Number of Mutants</th>
                        <th>Mutation Coverage</th>
                    </tr>
                </thead>
                <tbody>

        """

        reportMiddle = """
                </tbody>
            </table>
            <h3>Detailed List</h3>
                        <a href=\"original.java\">original file</a><br />

            <table>
            <thead>
                <tr>
                    <th>Survived Mutant</th>
                    <th>Build Output</th>
                    <th>Killed Mutant</th>
                    <th>Build Output</th>
                </tr>
            </thead>
            <tbody>
        """

        reportEnd = """
            </tbody>
        </table>
        <br/>
        <hr/> Report generated by LittleDarwin 0.4
        </body>
        </html>
        """

        output = list()
        joinedList = list()

        if len(survived) > len(killed):
            maxIndex = len(survived)
        else:
            maxIndex = len(killed)

        assert isinstance(survived, list)
        assert isinstance(killed, list)

        for i in range(0, maxIndex):
            try:
                survivedItem = survived[i]
            except IndexError as e:
                survivedItem = None

            try:
                killedItem = killed[i]
            except IndexError as e:
                killedItem = None

            joinedList.append([os.path.relpath(os.path.join(os.path.dirname(reportPath), survivedItem),
                                               os.path.dirname(reportPath)) if survivedItem is not None else None,
                               survivedItem, os.path.relpath(
                    os.path.join(os.path.dirname(reportPath), os.path.splitext(survivedItem)[0] + ".txt"),
                    os.path.dirname(reportPath)) if survivedItem is not None else None,
                               os.path.splitext(survivedItem)[0] + ".txt" if survivedItem is not None else None,
                               os.path.relpath(os.path.join(os.path.dirname(reportPath), killedItem),
                                               os.path.dirname(reportPath)) if killedItem is not None else None,
                               killedItem, os.path.relpath(
                    os.path.join(os.path.dirname(reportPath), os.path.splitext(killedItem)[0] + ".txt"),
                    os.path.dirname(reportPath)) if killedItem is not None else None,
                               os.path.splitext(killedItem)[0] + ".txt" if killedItem is not None else None])

        fileOverallStats = "<tr><td>" + str(len(survived) + len(killed)) + " </td> <td> " + ("%3.1f" % (
            float(len(killed)) / float(len(survived) + len(
                killed)) * 100)) + "  <div class=\"coverage_bar\"><div class=\"coverage_complete\" style=\"width:" + (
                               "%d" % (float(len(killed)) / float(
                                   len(survived) + len(
                                       killed)) * 100)) + "%\"></div><div class=\"coverage_legend\">" + str(
            len(killed)) + "/" + str(len(killed) + len(survived)) + "</div></div></td></tr>"

        for item in joinedList:
            output.append(
                "<tr><td><a href=\"" + xstr(item[0]) + "\">" + xstr(item[1]) + "</a></td> <td><a href=\"" + xstr(
                    item[2]) + "\">" + xstr(item[3]) + "</a></td><td><a href=\"" + xstr(item[4]) + "\">" + xstr(
                    item[5]) + "</a></td><td><a href=\"" + xstr(item[6]) + "\">" + xstr(item[7]) + "</a></td></tr>")

        reportOutput = list()
        reportOutput.extend([reportBeginning, fileOverallStats, reportMiddle])
        reportOutput.extend(output)
        reportOutput.append(reportEnd)

        return '\n'.join(reportOutput)
