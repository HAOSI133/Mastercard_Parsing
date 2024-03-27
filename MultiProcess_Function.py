import multiprocessing
import urllib
import sqlalchemy as sa
import sys
import pandas as pd
import numpy as np
from Logger import Logger

logger = Logger().logger
log_exception = Logger().log_exception

def insert_chunk(chunk):
    try:
        connection_string = 'Driver={' + str('SQL Server') + '};Server=' + 'BPLDEVDB01' + ';Database=' + 'Srijan_PLAT_CI' + ';Trusted_Connection=yes;MultiSubnetFailover=Yes;'
        connection_uri = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = sa.create_engine(connection_uri, echo=False, fast_executemany=True)
        chunk.to_sql('IPMMasterInterim', engine, schema=".dbo", if_exists="append", index=False,chunksize = 1500)
    except Exception as e:
        logger.error(f"Error occour while inserting {e}")
        log_exception(*sys.exc_info())
    
def insert_to_Sql(List_Value):
    try:
        #CSV_Header = ['MTI', 'DE3', 'DE4', 'DE5', 'DE6', 'DE9', 'DE10', 'DE12', 'DE14', 'DE22', 'DE23', 'DE24', 'DE25', 'DE26', 'DE30', 'DE31', 'DE32', 'DE33', 'DE37', 'DE38', 'DE40', 'DE41', 'DE42', 'DE43', 'DE48', 'DE49', 'DE50', 'DE51', 'DE54', 'DE55', 'DE62', 'DE63', 'DE71', 'DE72', 'DE73', 'DE93', 'DE94', 'DE95', 'DE100', 'DE111', 'DE123', 'DE124', 'DE125', 'DE126', 'DE127', 'PDS0001', 'PDS0002', 'PDS0003', 'PDS0004', 'PDS0005', 'PDS0006', 'PDS0014', 'PDS0015', 'PDS0017', 'PDS0018', 'PDS0021', 'PDS0022', 'PDS0023', 'PDS0025', 'PDS0026', 'PDS0028', 'PDS0029', 'PDS0042', 'PDS0043', 'PDS0044', 'PDS0045', 'PDS0046', 'PDS0052', 'PDS0056', 'PDS0057', 'PDS0058', 'PDS0059', 'PDS0068', 'PDS0071', 'PDS0072', 'PDS0080', 'PDS0105', 'PDS0106', 'PDS0110', 'PDS0122', 'PDS0137', 'PDS0138', 'PDS0140', 'PDS0141', 'PDS0145', 'PDS0146', 'PDS0147', 'PDS0148', 'PDS0149', 'PDS0157', 'PDS0158', 'PDS0159', 'PDS0160', 'PDS0164', 'PDS0165', 'PDS0170', 'PDS0171', 'PDS0172', 'PDS0173', 'PDS0174', 'PDS0175', 'PDS0176', 'PDS0177', 'PDS0178', 'PDS0179', 'PDS0180', 'PDS0181', 'PDS0182', 'PDS0183', 'PDS0184', 'PDS0185', 'PDS0186', 'PDS0188', 'PDS0189', 'PDS0190', 'PDS0191', 'PDS0192', 'PDS0194', 'PDS0195', 'PDS0196', 'PDS0197', 'PDS0198', 'PDS0199', 'PDS0200', 'PDS0202', 'PDS0204', 'PDS0205', 'PDS0206', 'PDS0207', 'PDS0208', 'PDS0209', 'PDS0210', 'PDS0211', 'PDS0212', 'PDS0213', 'PDS0214', 'PDS0215', 'PDS0220', 'PDS0221', 'PDS0222', 'PDS0225', 'PDS0228', 'PDS0230', 'PDS0241', 'PDS0243', 'PDS0244', 'PDS0245', 'PDS0246', 'PDS0247', 'PDS0248', 'PDS0249', 'PDS0250', 'PDS0251', 'PDS0252', 'PDS0253', 'PDS0254', 'PDS0255', 'PDS0260', 'PDS0261', 'PDS0262', 'PDS0264', 'PDS0265', 'PDS0266', 'PDS0267', 'PDS0268', 'PDS0280', 'PDS0300', 'PDS0301', 'PDS0302', 'PDS0306', 'PDS0358', 'PDS0359', 'PDS0367', 'PDS0368', 'PDS0369', 'PDS0370', 'PDS0372', 'PDS0374', 'PDS0375', 'PDS0378', 'PDS0380', 'PDS0381', 'PDS0384', 'PDS0390', 'PDS0391', 'PDS0392', 'PDS0393', 'PDS0394', 'PDS0395', 'PDS0396', 'PDS0397', 'PDS0398', 'PDS0399', 'PDS0400', 'PDS0401', 'PDS0402', 'PDS0446', 'PDS0501', 'PDS0502', 'PDS0503', 'PDS0504', 'PDS0505', 'PDS0506', 'PDS0507', 'PDS0508', 'PDS0509', 'PDS0510', 'PDS0511', 'PDS0512', 'PDS0513', 'PDS0514', 'PDS0515', 'PDS0516', 'PDS0517', 'PDS0518', 'PDS0519', 'PDS0520', 'PDS0521', 'PDS0522', 'PDS0523', 'PDS0524', 'PDS0525', 'PDS0526', 'PDS0527', 'PDS0528', 'PDS0529', 'PDS0530', 'PDS0531', 'PDS0532', 'PDS0533', 'PDS0534', 'PDS0535', 'PDS0536', 'PDS0537', 'PDS0538', 'PDS0539', 'PDS0540', 'PDS0541', 'PDS0542', 'PDS0543', 'PDS0544', 'PDS0545', 'PDS0546', 'PDS0547', 'PDS0548', 'PDS0549', 'PDS0550', 'PDS0551', 'PDS0552', 'PDS0553', 'PDS0554', 'PDS0555', 'PDS0556', 'PDS0557', 'PDS0558', 'PDS0559', 'PDS0560', 'PDS0561', 'PDS0562', 'PDS0563', 'PDS0564', 'PDS0565', 'PDS0566', 'PDS0567', 'PDS0568', 'PDS0569', 'PDS0570', 'PDS0571', 'PDS0572', 'PDS0573', 'PDS0574', 'PDS0575', 'PDS0576', 'PDS0577', 'PDS0578', 'PDS0579', 'PDS0580', 'PDS0581', 'PDS0582', 'PDS0583', 'PDS0584', 'PDS0585', 'PDS0586', 'PDS0587', 'PDS0588', 'PDS0589', 'PDS0590', 'PDS0591', 'PDS0592', 'PDS0593', 'PDS0594', 'PDS0595', 'PDS0596', 'PDS0597', 'PDS0598', 'PDS0599', 'PDS0600', 'PDS0601', 'PDS0602', 'PDS0603', 'PDS0604', 'PDS0605', 'PDS0606', 'PDS0607', 'PDS0608', 'PDS0609', 'PDS0610', 'PDS0611', 'PDS0612', 'PDS0613', 'PDS0614', 'PDS0615', 'PDS0616', 'PDS0617', 'PDS0618', 'PDS0619', 'PDS0620', 'PDS0621', 'PDS0622', 'PDS0623', 'PDS0624', 'PDS0625', 'PDS0626', 'PDS0627', 'PDS0628', 'PDS0629', 'PDS0630', 'PDS0631', 'PDS0632', 'PDS0633', 'PDS0634', 'PDS0635', 'PDS0636', 'PDS0637', 'PDS0638', 'PDS0639', 'PDS0640', 'PDS0641', 'PDS0642', 'PDS0643', 'PDS0644', 'PDS0645', 'PDS0646', 'PDS0647', 'PDS0648', 'PDS0649', 'PDS0650', 'PDS0651', 'PDS0652', 'PDS0653', 'PDS0654', 'PDS0655', 'PDS0656', 'PDS0657', 'PDS0658', 'PDS0659', 'PDS0660', 'PDS0661', 'PDS0662', 'PDS0663', 'PDS0664', 'PDS0665', 'PDS0666', 'PDS0667', 'PDS0668', 'PDS0669', 'PDS0670', 'PDS0671', 'PDS0672', 'PDS0673', 'PDS0674', 'PDS0675', 'PDS0676', 'PDS0677', 'PDS0678', 'PDS0679', 'PDS0680', 'PDS0681', 'PDS0682', 'PDS0683', 'PDS0684', 'PDS0685', 'PDS0686', 'PDS0687', 'PDS0688', 'PDS0689', 'PDS0690', 'PDS0691', 'PDS0692', 'PDS0693', 'PDS0694', 'PDS0695', 'PDS0696', 'PDS0697', 'PDS0698', 'PDS0699', 'PDS0700', 'PDS0701', 'PDS0702', 'PDS0703', 'PDS0704', 'PDS0705', 'PDS0706', 'PDS0707', 'PDS0708', 'PDS0709', 'PDS0710', 'PDS0711', 'PDS0712', 'PDS0713', 'PDS0714', 'PDS0715', 'PDS0716', 'PDS0717', 'PDS0718', 'PDS0719', 'PDS0720', 'PDS0721', 'PDS0722', 'PDS0723', 'PDS0724', 'PDS0725', 'PDS0726', 'PDS0727', 'PDS0728', 'PDS0729', 'PDS0730', 'PDS0731', 'PDS0732', 'PDS0733', 'PDS0734', 'PDS0735', 'PDS0736', 'PDS0737', 'PDS0738', 'PDS0739', 'PDS0740', 'PDS0741', 'PDS0742', 'PDS0743', 'PDS0744', 'PDS0745', 'PDS0746', 'PDS0747', 'PDS0748', 'PDS0749', 'PDS0750', 'PDS0751', 'PDS0752', 'PDS0753', 'PDS0754', 'PDS0755', 'PDS0756', 'PDS0757', 'PDS0758', 'PDS0759', 'PDS0760', 'PDS0761', 'PDS0762', 'PDS0763', 'PDS0764', 'PDS0765', 'PDS0770', 'PDS0771', 'PDS0772', 'PDS0773', 'PDS0774', 'PDS0775', 'PDS0776', 'PDS0777', 'PDS0799', 'PDS10xx', 'BinNumber', 'PanHash', 'CardNumber4Digits', 'ProcCode', 'ProcCodeFromAccType', 'ProcCodeToAccType', 'DateTimeLocalTxn']
        CSV_Header = ['TranId' ,'MessageTypeIdentifier' ,'ProcCode' ,'ProcCodeFromAccType' ,'ProcCodeToAccType' ,'TransactionAmount' ,'TxnSrcAmt' ,'SettlementAmount' ,'ConversionRateSettlement' ,'AmountCurrencyConversionAssessment' ,'DateLocalTransaction' ,'TimeLocalTransaction' ,'ExpirationDate' ,'POSInputCap' ,'POSCardHolderAuthCap' ,'POSCardCaptureCapabilities' ,'POSTermOpEnv' ,'POSCardholderPresenceInd' ,'POSCardPresenceIndicator' ,'POSCardDataInputMode' ,'POSCardmemberAuth' ,'POSCardmemberAuthEntity' ,'POSCardDataOutputCapability' ,'POSTerminalOutputCapability' ,'PINEntryCapability' ,'CardSequenceNumber' ,'FunctionCode' ,'MessageReasonCode' ,'AmountOrgRecon' ,'MerchantType' ,'AmountOrgTran' ,'AcquirerID' ,'SeqNumAcqDet' ,'CheckDigit' ,'JulianProSubDate' ,'AcquiringInsitutionIDCode' ,'ForwardingInsitutionIDCode' ,'RetrievalReferenceNumber' ,'ApprovalCode' ,'ServiceCode' ,'CardAcceptorTerminalID' ,'CardAcceptorIdCode' ,'MerchantName' ,'MerchantStreetAddress' ,'MerchantCity' ,'MerchantLocPostalCode' ,'MerchantStProvCode' ,'MerchantStateProvinceCode' ,'MerchantCountry' ,'MerchantCountryCode' ,'TransactionCurrencyCode' ,'SettlementCurrencyCode' ,'CardholderBillingAmount' ,'ConvRateCardholderBilling' ,'InterchangeFeeIndicator' ,'ConditionID' ,'AccountType' ,'AmountType' ,'CurrencyCode' ,'AmountSign' ,'Amount' ,'AdditionalAmount' ,'PrimaryCurrencyCode' ,'SecondaryCurrencyCode' ,'TertiaryCurrencyCode' ,'AccountType1' ,'AmountType1' ,'CurrencyCode1' ,'AmountSign1' ,'Amount1' ,'AccountType2' ,'AmountType2' ,'CurrencyCode2' ,'AmountSign2' ,'Amount2' ,'AmountType3' ,'AccountType3' ,'CurrencyCode3' ,'AmountSign3' ,'Amount3' ,'AccountType4' ,'AmountType4' ,'CurrencyCode4' ,'AmountSign4' ,'Amount4' ,'AccountType5' ,'AmountType5' ,'CurrencyCode5' ,'AmountSign5' ,'Amount5' ,'ApplicationCryptogram' ,'CryptogramInformationData' ,'IssuerApplicationData' ,'UnpredictableNumber' ,'ApplicationTxnCounter' ,'TerminalVerificationResult' ,'Transactiondate' ,'TransactionType' ,'AuthorizedAmount' ,'TransactionCurrencyCodeICC' ,'ApplicationInterchangeProfile' ,'TerminalCountryCode' ,'OtherAmount' ,'TerminalType_ICC9F35' ,'TerminalApplicationversionNumber_ICC9F09' ,'InterfaceDeviceSerialNumber_ICC9F1E' ,'TerminalCapabilities_ICC9F33' ,'CardholderVerificationMethodResults_ICC9F34' ,'TransactionSequenceCounter_ICC9F41' ,'TransactionCategoryCode_ICC9F53' ,'DedicatedFileName_ICC84' ,'ICCSysRelatedData' ,'IssuerAppData' ,'LifeCycleSupportIndicator' ,'MessageNumber' ,'BankNetDate' ,'DataRecordInitial' ,'ActionDate' ,'CardIssuerRefData' ,'AccountTypePDS' ,'CurrCodeCardHolderBilling' ,'JobStatus' ,'TranTime' ,'PostTime' ,'CaseID' ,'DriverNumberIDNumber' ,'MessageDirection' ,'PartialAmountIndicator' ,'OutgoingStatus' ,'TransacOriginatorInstIDCode' ,'CardAcceptorNameLocation' ,'ResponseCode' ,'NetworkReferenceID' ,'TheFinancialNetworkCode' ,'AuthorizationResponseCode' ,'NetworkName' ,'TraceID' ,'CashBackAmount' ,'PaymentTransactionTypeIndicator' ,'ReceivingICANumber' ,'SendingICANumber' ,'gcmsproductidentifier' ,'mtMSMCAdditional' ,'RecordData' ,'ReceivingInstIDCode' ,'UniqueID' ,'JobId' ,'MotorFuelQuantity' ,'MotorFuelSaleAmount' ,'MotorFuelUnitPrice' ,'StateCountryCode' ,'TokenRequestorID' ,'VehicleNumber' ,'CurrencyCode13' ,'CreditDebit15' ,'Amount16' ,'CurrencyCode23' ,'CreditDebit25' ,'Amount26' ,'CurrencyCode33' ,'CreditDebit35' ,'Amount36' ,'CurrencyCode43' ,'CreditDebit45' ,'Amount46' ,'CurrencyCode53' ,'CreditDebit55' ,'Amount56' ,'CurrencyCode63' ,'CreditDebit65' ,'Amount66' ,'AuxillaryField1_00PDS' ,'AuxillaryField2_00PDS' ,'AuxillaryField1_01PDS' ,'AuxillaryField2_01PDS' ,'AuxillaryField1_02PDS' ,'AuxillaryField2_02PDS' ,'AuxillaryField1_03PDS' ,'AuxillaryField2_03PDS' ,'AuxillaryField1_04PDS' ,'AuxillaryField2_04PDS' ,'OriginalTerminalType' ,'TerminalType' ,'MessageReversalIndicator' ,'CentSiteProcDateOFile' ,'ProgramRegistrationID' ,'MessageReversalInd' ,'CentSiteProcDateOMess' ,'SecurityProtocol' ,'CardHolderAuthentication' ,'UCAFCollectionIndicator' ,'TxnCategoryIndicator' ,'MCElectronicCardIndicator' ,'TaxAmountRateTypeCode' ,'TaxAmountValueAddedTax' ,\
                            'TaxAmountCurrencyCode' ,'TaxAmountCurrencyExponent' ,'TaxAmountDebitCreditIndicator' ,'FeeCollectionControlNumber' ,'TransmissionDateTime' ,'AlternateTransactionFee_CurrencyCode' ,'AlternateTransactionFee_Amount' ,'FeeTypeCodeTxnFee1' ,'FeeProcessCodeTxnFee1' ,'FeeSettleIndicator1' ,'CurrencyCodeFee1' ,'AmountFeeTxnFee1' ,'CurrencyCodeFeeRecon1' ,'AmountFeeRecon1' ,'FeeTypeCodeTxnFee2' ,'FeeProcessCodeTxnFee2' ,'FeeSettleIndicator2' ,'CurrencyCodeFee2' ,'AmountFeeTxnFee2' ,'CurrencyCodeFeeRecon2' ,'AmountFeeRecon2' ,'FeeTypeCodeTxnFee3' ,'FeeProcessCodeTxnFee3' ,'FeeSettleIndicator3' ,'CurrencyCodeFee3' ,'AmountFeeTxnFee3' ,'CurrencyCodeFeeRecon3' ,'AmountFeeRecon3' ,'FeeTypeCodeTxnFee4' ,'FeeProcessCodeTxnFee4' ,'FeeSettleIndicator4' ,'CurrencyCodeFee4' ,'AmountFeeTxnFee4' ,'CurrencyCodeFeeRecon4' ,'AmountFeeRecon4' ,'FeeTypeCodeTxnFee5' ,'FeeProcessCodeTxnFee5' ,'FeeSettleIndicator5' ,'CurrencyCodeFee5' ,'AmountFeeTxnFee5' ,'CurrencyCodeFeeRecon5' ,'AmountFeeRecon5' ,'FeeTypeCodeTxnFee6' ,'FeeProcessCodeTxnFee6' ,'FeeSettleIndicator6' ,'CurrencyCodeFee6' ,'AmountFeeTxnFee6' ,'CurrencyCodeFeeRecon6' ,'AmountFeeRecon6' ,'FeeTypeCodeTxnFee7' ,'FeeProcessCodeTxnFee7' ,'FeeSettleIndicator7' ,'CurrencyCodeFee7' ,'AmountFeeTxnFee7' ,'CurrencyCodeFeeRecon7' ,'AmountFeeRecon7' ,'FeeTypeCodeTxnFee8' ,'FeeProcessCodeTxnFee8' ,'FeeSettleIndicator8' ,'CurrencyCodeFee8' ,'AmountFeeTxnFee8' ,'CurrencyCodeFeeRecon8' ,'AmountFeeRecon8' ,'FeeTypeCodeTxnFee9' ,'FeeProcessCodeTxnFee9' ,'FeeSettleIndicator9' ,'CurrencyCodeFee9' ,'AmountFeeTxnFee9' ,'CurrencyCodeFeeRecon9' ,'AmountFeeRecon9' ,'FeeTypeCodeTxnFee10' ,'FeeProcessCodeTxnFee10' ,'FeeSettleIndicator10' ,'CurrencyCodeFee10' ,'AmountFeeTxnFee10' ,'CurrencyCodeFeeRecon10' ,'AmountFeeRecon10' ,'FeeTypeCodeTxnFee11' ,'FeeProcessCodeTxnFee11' ,'FeeSettleIndicator11' ,'CurrencyCodeFee11' ,'AmountFeeTxnFee11' ,'CurrencyCodeFeeRecon11' ,'AmountFeeRecon11' ,'FeeTypeCodeTxnFee12' ,'FeeProcessCodeTxnFee12' ,'FeeSettleIndicator12' ,'CurrencyCodeFee12' ,'AmountFeeTxnFee12' ,'CurrencyCodeFeeRecon12' ,'AmountFeeRecon12' ,'CurrencyExponent' ,'CurrencyCode1_148' ,'CurrencyExponent1' ,'CurrencyCode2_148' ,'CurrencyExponent2' ,'CurrencyCode3_148' ,'CurrencyExponent3' ,'CurrencyCode4_148' ,'CurrencyExponent4' ,'CurrencyCode5_148' ,'CurrencyExponent5' ,'CurrencyCode6' ,'CurrencyExponent6' ,'CurrencyCode7' ,'CurrencyExponent7' ,'CurrencyCode8' ,'CurrencyExponent8' ,'CurrencyCode9' ,'CurrencyExponent9' ,'CurrencyCode10' ,'CurrencyExponent10' ,'CurrencyCode11' ,'CurrencyExponent11' ,'CurrencyCode12' ,'CurrencyExponent12' ,'CurrencyExponent13' ,'CurrencyCode14' ,'CurrencyExponent14' ,'CurrencyCode15' ,'CurrencyExponent15' ,'CurrencyCodeOriginalTxnAmount' ,'CurrencyCodeOrgReconAmount' ,'AlternateProcessorIndicator' ,'MCAssignedIDOvrrideIndicator' ,'FutureUse1_PDS0044' ,'PDS0158FutureUse11' ,'PDS0158FutureUse13' ,'PDS0158FutureUse14' ,'AcceptanceBrandIDcode' ,'BusinessServiceIDCode' ,'BusinessServiceLevelCode' ,'mccoverrideindicator' ,'productoverrideindicator' ,'rateapplyindicator' ,'BusinessDate' ,'BusinessCycle' ,'SettlementAgreementInfo' ,'SettlementIndicator' ,'DocumentationIndicator' ,'deInterchangeRateIndicator_Out' ,'InterchangeRateIndicator' ,'CharacterSetIndicator' ,'AdditionalContactInfo' ,'MerchantTelephoneNumber' ,'MerchantDescriptionData' ,'SoleProprietorName' ,'LegalCorporateName' ,'DUN_Dun_Bradstreet' ,'CrossBorderIndicator' ,'CurrencyIndicator' ,'CharacterSetIndicator2' ,'CardAcceptorDataDesc' ,'CardAcceptorURL' ,'MerchantID' ,'TypeofInstallments' ,'NumberofInstallments' ,'InterestRatePDS0181' ,'FirstInstallmentAmountPDS0181' ,'SubsequentInstallmentAmountPDS0181' ,'AnnualPercentRatePDS0181' ,'InstallmentFeePDS0181' ,'CommissionRatePDS0181' ,'CommissionSignPDS0181' ,'CommissionAmountPDS0181' ,'BankNetReferenceNumber' ,'FormatNumber' ,'PhoneData' ,'PartnerIdCode' ,'PaymentTransactionInitiator' ,'OriginatingMessageFormat' ,'RemotePymtsProgData' ,'TNumberofInstallments' ,'InstallmentOption' ,'InstallmentNumber' ,'BonusCode' ,'BonusMonthCode' ,'NoOfPayementPerYr' ,'BonusAmount' ,'FirstMonthBonusPayement' ,'MobilePhoneNumber' ,'MPhoneServiceProvider' ,\
                                'TaxAmount1' ,'TaxAmount2' ,'TaxPercentage' ,'TaxBaseAmount' ,'TaxAmount3' ,'PrimaryAcctNbrSyntErr' ,'AmountSyntErr' ,'DataElementID' ,'ErrorSeverityCode' ,'ErrorMessageCode' ,'SubfieldID' ,'ATMLatePresentmentIndicator' ,'NbrDaysSinceTranOccurred' ,'WalletIdentifier' ,'TransitTranTypeIndicator' ,'TranspModeIndicator' ,'ConvertedToAccountNumber' ,'RetrievalDocumentCode' ,'MCControlNo' ,'DateFirstReturnBus' ,'EditExclResultsCode' ,'MCIssRetrievalReqDate' ,'MCAcqRetrievalRespCode' ,'MCAcqRetrievalRespSentDate' ,'MCIssuerResponseCode' ,'MCIssuerResponseDate' ,'MCIssuerRejectReasons' ,'MCImageReviewDecision' ,'MCImageReviewDate' ,'MCCbackSuppDocDate1' ,'MCCbackDocProcDate2P' ,'MasterComSenderMemo' ,'MasterComReceiverMemo' ,'MasterComImageReviewMemo_PDS0248' ,'MasterComRecordId' ,'MasterComSenderEndpointNbr' ,'MasterComRecieverEndpointNbr' ,'MasterComSystemEnhancedData' ,'MasterComMemberEnhancedData' ,'MasterComMessageType' ,'MCPreferedAcqrEndPoint' ,'ExclusionRequestCode' ,'ExclusionReasonCode' ,'ExclusionResultsCode' ,'InterchangeLifeCycleValidationCode' ,'DocIndicator' ,'InitialMessageReasonCode' ,'DateInitialPresentmtBussiness' ,'EditExclReasonCode' ,'AmountFirstReturn' ,'CurrCodeFirstReturn' ,'DataRecFirstReturn' ,'MessageReasonCodeSec' ,'DateSecondReturnBus' ,'AmountSecondReturn' ,'CurrCodeSecondReturn' ,'DataRecSecondReturn' ,'AmountPartialTransaction' ,'CurrencyCodePartialTransaction' ,'SettlementTransferAgentID' ,'SettleTransferAgentAcct' ,'SettlementLevelCode' ,'SettlementServiceIDCode' ,'SettleForeignExchRateClass' ,'SettlementDate' ,'SettlementCycle' ,'MemberReconIndicator1' ,'TranFeeAmtSyntErr' ,'CustomerServiceNumber' ,'MemberToMemberProprietary_PDS1000' ,'TotalTransactionNumber' ,'AmountTransaction' ,'AmtTranInTranCurr' ,'VirtualAccountNumber' ,'FileReversalIndicator' ,'SourceMessageNumberID' ,'CardProgramIdentifier' ,'BussinessServiceAgreementTypeCode' ,'deBusinessServiceIDCode' ,'SourceFileType' ,'SourceFileReferenceDate' ,'SourceProcessorID' ,'SourceFileSeqNumber' ,'PDSData' ,'ReconFileType' ,'ReconFileReferenceDate' ,'ReconProcessorID' ,'ReconFileSeqNumber' ,'ReconciledMemberActivity' ,'ReconAcceptBrandIdCode' ,'ReconBusiServiceLevelCode' ,'ReconBusinessServiceIDCode' ,'ReconInterchgRateIndicator' ,'ReconBusinessDate' ,'ReconBusinessCycle' ,'ReconFunctionCode' ,'ReconMsgTypeIdentifier' ,'ReconProcessingCode' ,'ReconSettleTransferAgentID' ,'ReconSettleTransAgentAcct' ,'ReconSettleLevelCode' ,'ReconSettleServiceIDCode' ,'ReconSettleExchgRateClass' ,'ReconReconciliationCycle' ,'ReconReconciliationDate' ,'ReconSettlementDate' ,'ReconSettlementCycle' ,'ReconciledCardProgramIdentifier' ,'ReconciledTransactionFunctionGroupCode' ,'ReconciledAcquirerBIN' ,'MCAssignedIDOvrrideIndicator2' ,'PDS0358FutureUse12' ,'PDS0358FutureUse13' ,'PDS0358FutureUse14' ,'BeginingAcctRangeID' ,'EndingAcctRangeID' ,'OriginalReversalTotalIndicator' ,'deCreditDebitIndicator1_Out' ,'deCreditDebitIndicator2_Out' ,'AmountNetUnsigned' ,'deCreditDebitIndicator3_Out' ,'AmtTranDrInReconCurr' ,'deCreditDebitIndicator4_Out' ,'AmtTranCrInReconCurr' ,'deCreditDebitIndicator5_Out' ,'deCreditDebitIndicator6_Out' ,'deCreditDebitIndicator7_Out' ,'AmtNetInReconCurr' ,'deCreditDebitIndicator8_Out' ,'AmtNetFeeInReconCurr' ,'deCreditDebitIndicator9_Out' ,'AmountNetTotalUnsigned' ,'deCreditDebitIndicator10_Out' ,'DebitsTransactionNumber' ,'CreditsTransactionNumber' ,'PDS0397' ,'PDS0398' ,'PDS0399' ,'PAN_Hash' ,'CardNumber4Digits' ,'BINNumber' ,'ChargeAssmtFee' ,'LoyaltyFlag' ,'AcquirerRefNumber' ,'TokenUniqueReference' ,'PANUniqueReference' ,'PaymentHash' ,'ATMStateProvCode' ,'CallOriginStateCode' ,'ProgramParticipationIndicator' ,'IPMOrgTerminalType' ,'IPM_POSCardDataInputMode' ,'IPMCrossBorderIndicator' ,'CPSEnvironment' ,'DigitalWalletIntrchngOverrideIndic0158' ,'DigitalWalletIntrchngOverrideIndic0358' ,'DomesticMerchantTaxID_0221' ,'FinancialAcctInfo_0068' ,\
                                    'BS_SystemStatus' ,'TranIdOriginal' ,'PODId_FileReceived' ,'PANHash64' ,'IPM_AlgorithmID' ,'Outstg_Status' ,'CardAcceptorIdCode_upd' ,'AcquiringInsitutionIDCode_upd' ,'TransactionDescription' ,'Reversed' ,'creditplanmaster' ,'MessageIndicator' ,'CardDataEntryMode' ,'TxnCreated' ,'CardholderBillingAmountOrg' ,'CurrCodeCardHolderBillingOrg' ,'DateLocalTransactionOrg' ,'TimeLocalTransactionOrg' ,'JulianProSubDateOrg' ,'ExpirationDateOrg' ,'CardDataEntryModeOrg' ,'MessageReasonCodeOrg' ,'BinNumberPDS0001' ,'IsPartialClr' , 'IPMCardPresent', 'IsCreditTxn' ,'CardExpirationDate' ,'TLID']

        df = pd.DataFrame(List_Value, columns = CSV_Header)
        num_core = multiprocessing.cpu_count()
        num_core = min(multiprocessing.cpu_count(), len(List_Value))
        splits = np.array_split(df,num_core)
        pool = multiprocessing.Pool(num_core)
        pool.map(insert_chunk,splits)
        pool.close()
        pool.join()
        del df
    except Exception as e:
        logger.error(f"Error occour while inserting {e}")
        log_exception(*sys.exc_info())