import 'package:flutter/material.dart';
import 'package:reffin_ach/reffin_ach.dart';

void main() {
  runApp(const AchExampleApp());
}

class AchExampleApp extends StatelessWidget {
  const AchExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    final checkingCredit = resolveTransactionCode('22')!;
    final invalidIndividualId = resolveReturnCode('r22')!;
    final futureSanctionsReturn = resolveReturnCodeAsOf(
      'R90',
      DateTime.utc(2028, 3, 17),
    )!;

    return MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text('ACH reference codes')),
        body: ListView(
          children: [
            ListTile(
              leading: Icon(checkingCredit.icon),
              title: Text('${checkingCredit.code}: ${checkingCredit.name}'),
              subtitle: Text('${checkingCredit.accountType} / ${checkingCredit.direction}'),
            ),
            ListTile(
              leading: Icon(invalidIndividualId.icon),
              title: Text('${invalidIndividualId.code}: ${invalidIndividualId.name}'),
              subtitle: Text(invalidIndividualId.category),
            ),
            ListTile(
              leading: Icon(futureSanctionsReturn.icon),
              title: Text('${futureSanctionsReturn.code}: ${futureSanctionsReturn.name}'),
              subtitle: const Text('Effective March 17, 2028'),
            ),
          ],
        ),
      ),
    );
  }
}
